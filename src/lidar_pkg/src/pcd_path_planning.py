#!/usr/bin/env python3

import numpy as np
import rospy
import sensor_msgs.point_cloud2 as pc2
from sensor_msgs.msg import PointCloud2
import std_msgs.msg
from sklearn.svm import SVC

def pointcloud_callback(msg):
    global midpoints

    pc_data = pc2.read_points(msg, skip_nans=True, field_names=("x", "y", "z"))
    pc_array = np.array(list(pc_data))

    left_lane = []
    right_lane = []
    for point in pc_array:
        x, y, z = point
        if x > -1:
            left_lane.append((x, y))
        else:
            right_lane.append((x, y))

    left_lane = np.array(left_lane)
    right_lane = np.array(right_lane)

    X = np.vstack((left_lane, right_lane))
    y = np.hstack((np.zeros(len(left_lane)), np.ones(len(right_lane))))

    model = SVC(kernel='rbf', C=10.0, gamma='scale')
    model.fit(X, y)

    xx, yy = np.meshgrid(np.linspace(min(X[:, 0]), max(X[:, 0]), 100), np.linspace(min(X[:, 1]), max(X[:, 1]), 100))
    Z = model.decision_function(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    # 결정 경계 근처의 점들을 찾습니다.
    contour_mask = np.abs(Z) < 0.05

    xs = xx[contour_mask]
    ys = yy[contour_mask]

    # x 값을 기준으로 일정 간격의 인덱스를 선택합니다.
    num_points = 20
    idxs = np.linspace(0, len(xs) - 1, num_points).astype(int)
    selected_xs = xs[idxs]
    selected_ys = ys[idxs]

    midpoints = np.column_stack((selected_xs, selected_ys, np.zeros_like(selected_xs)))

    header = std_msgs.msg.Header()
    header.stamp = rospy.Time.now()
    header.frame_id = msg.header.frame_id

    fields = [
        pc2.PointField('x', 0, pc2.PointField.FLOAT32, 1),
        pc2.PointField('y', 4, pc2.PointField.FLOAT32, 1),
        pc2.PointField('z', 8, pc2.PointField.FLOAT32, 1),
    ]

    pc_msg = pc2.create_cloud(header, fields, midpoints)
    pub.publish(pc_msg)


def listener():
    rospy.init_node('pointcloud_listener', anonymous=True)
    rospy.Subscriber('/object_centroids', PointCloud2, pointcloud_callback)
    rospy.spin()

if __name__ == '__main__':
    pub = rospy.Publisher('/path_planning', PointCloud2, queue_size=10)
    listener()
