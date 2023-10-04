#!/usr/bin/env python3
from sklearn.linear_model import LinearRegression
import numpy as np
import rospy
import sensor_msgs.point_cloud2 as pc2
from sensor_msgs.msg import PointCloud2
import std_msgs.msg
from sklearn.cluster import DBSCAN
from sklearn.svm import SVC

def create_cloud_msg(points, frame_id):
    header = std_msgs.msg.Header()
    header.stamp = rospy.Time.now()
    header.frame_id = frame_id

    fields = [
        pc2.PointField('x', 0, pc2.PointField.FLOAT32, 1),
        pc2.PointField('y', 4, pc2.PointField.FLOAT32, 1),
        pc2.PointField('z', 8, pc2.PointField.FLOAT32, 1),
    ]

    return pc2.create_cloud(header, fields, points)

def pointcloud_callback(msg):
    pc_data = pc2.read_points(msg, skip_nans=True, field_names=("x", "y", "z"))
    pc_array = np.array(list(pc_data))

    # DBSCAN clustering
    clustering = DBSCAN(eps=4, min_samples=2).fit(pc_array[:, :2])
    labels = clustering.labels_
    unique_labels = np.unique(labels)

    closest_left_label, closest_right_label = None, None
    closest_left_distance, closest_right_distance = float('inf'), float('inf')

    # Compute distances only once
    distances = np.sqrt(np.sum(pc_array[:, :2]**2, axis=1))

    for label in unique_labels:
        if label == -1:  # Skip the noise points
            continue

        cluster_mask = labels == label
        cluster_points = pc_array[cluster_mask]

        # Find closest points in each cluster for left and right
        left_mask = cluster_points[:, 1] > 0
        right_mask = cluster_points[:, 1] < 0

        if np.any(left_mask):
            min_left_distance_idx = np.argmin(distances[cluster_mask][left_mask])
            min_left_distance = distances[cluster_mask][left_mask][min_left_distance_idx]
            if min_left_distance < closest_left_distance:
                closest_left_distance = min_left_distance
                closest_left_label = label

        if np.any(right_mask):
            min_right_distance_idx = np.argmin(distances[cluster_mask][right_mask])
            min_right_distance = distances[cluster_mask][right_mask][min_right_distance_idx]
            if min_right_distance < closest_right_distance:
                closest_right_distance = min_right_distance
                closest_right_label = label

    # Create point clouds for closest left and right points
    left_lane = pc_array[labels == closest_left_label] if closest_left_label is not None else np.array([])
    right_lane = pc_array[labels == closest_right_label] if closest_right_label is not None else np.array([])

    if len(right_lane) > 0:
        # Linear Regression to find the best fit line for right_lane
        reg = LinearRegression().fit(right_lane[:, 0].reshape(-1, 1), right_lane[:, 1])

        # Slope and intercept
        m = reg.coef_[0]
        c = reg.intercept_

        # Calculate the normal direction (perpendicular)
        normal_slope = -1 / m
        angle = np.arctan(normal_slope)
        dx = 2.5 * np.cos(angle)
        dy = 2.5 * np.sin(angle)

        # Determine if the vehicle is turning left or right based on the slope
        if m > 0:
            turning_left = True
        else:
            turning_left = False

        if turning_left:
            dx = -dx  # Change the sign
            dy = -dy  # Change the sign

        # Move the points of right_lane 2.5 units in the calculated direction
        new_right_lane = right_lane.copy()
        new_right_lane[:, 0] += dx
        new_right_lane[:, 1] += dy

        new_right_lane_msg = create_cloud_msg(new_right_lane, msg.header.frame_id)
        pub_new_right.publish(new_right_lane_msg)
    # Combine lanes for SVC
    X = np.vstack((left_lane[:, :2], right_lane[:, :2]))
    y = np.hstack((np.zeros(len(left_lane)), np.ones(len(right_lane))))

    if len(X) > 1:
        model = SVC(kernel='rbf', C=10, gamma='scale')
        model.fit(X, y)

    if len(left_lane) > 0:
        left_lane_msg = create_cloud_msg(left_lane, msg.header.frame_id)
        pub_left.publish(left_lane_msg)

    if len(right_lane) > 0:
        right_lane_msg = create_cloud_msg(right_lane, msg.header.frame_id)
        pub_right.publish(right_lane_msg)

    # if len(X) > 1:  # Ensure we have enough data points
    # Train an SVC model
    # model = SVC(kernel='rbf', C=10, gamma='scale')
    # model.fit(X, y)

    xx, yy = np.meshgrid(np.linspace(min(X[:, 0]), max(X[:, 0]), 100), np.linspace(min(X[:, 1]), max(X[:, 1]), 100))
    Z = model.decision_function(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    # Find points near the decision boundary
    contour_mask = np.abs(Z) < 0.05
    xs = xx[contour_mask]
    ys = yy[contour_mask]

    num_points = 20
    idxs = np.linspace(0, len(xs) - 1, num_points).astype(int)
    selected_xs = xs[idxs]
    selected_ys = ys[idxs]

    midpoints = np.column_stack((selected_xs, selected_ys, np.zeros_like(selected_xs)))

    midpoints = create_cloud_msg(midpoints, msg.header.frame_id)
    pub.publish(midpoints)

    print(midpoints)




def listener():
    rospy.init_node('pointcloud_listener', anonymous=True)
    rospy.Subscriber('/object_centroids', PointCloud2, pointcloud_callback)
    rospy.spin()

if __name__ == '__main__':
    pub = rospy.Publisher('/path_planning', PointCloud2, queue_size=10)
    pub_left = rospy.Publisher('/left_lane', PointCloud2, queue_size=10)
    pub_new_right = rospy.Publisher('/new_right_lane', PointCloud2, queue_size=10)    
    pub_right = rospy.Publisher('/right_lane', PointCloud2, queue_size=10)
    listener()
