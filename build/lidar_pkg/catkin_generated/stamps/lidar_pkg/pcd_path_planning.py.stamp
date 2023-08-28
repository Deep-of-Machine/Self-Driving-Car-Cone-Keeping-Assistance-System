#!/usr/bin/env python3

import numpy as np
import rospy
import sensor_msgs.point_cloud2 as pc2
from sensor_msgs.msg import PointCloud2
import std_msgs.msg

from scipy.spatial import Delaunay

def calculate_edge_midpoints(triangle):
    # Calculate the lengths of the edges
    edge_lengths = [np.linalg.norm(triangle[i] - triangle[(i+1)%3]) for i in range(3)]
    
    # Get the indices of the edges sorted by their lengths
    sorted_edge_indices = np.argsort(edge_lengths)

    # Get the midpoints of the two longest edges
    midpoints = [(triangle[i] + triangle[(i+1)%3])/2 for i in sorted_edge_indices[1:]]

    return midpoints

def find_centerline_path(left_lane, right_lane):
    # if len(left_lane) != len(right_lane):
    #     rospy.logwarn("왼쪽 차선과 오른쪽 차선의 점 개수가 같지 않습니다.")
    #     return np.array([])

    centerline = (left_lane + right_lane) / 2
    return centerline

def find_midpoints_of_lanes(left_lane, right_lane):
    # Combine the points from the left and right lanes
    points = np.vstack((left_lane, right_lane))

    if len(points) < 3:
        rospy.logwarn("점 개수가 충분하지 않습니다.")
        return np.array([])

    # If there are exactly three points, return the midpoint of the single triangle
    if len(points) == 3:
        triangle_midpoint = np.mean(points, axis=0)
        return np.array([triangle_midpoint])

    # Perform Delaunay triangulation
    tri = Delaunay(points)

    midpoints = []
    # Calculate and store the midpoints of the two longest edges of each triangle
    for indices in tri.simplices:
        triangle = points[indices]
        triangle_midpoints = calculate_edge_midpoints(triangle)
        midpoints.extend(triangle_midpoints)

    return np.array(midpoints)

def pointcloud_callback(msg):
    # midpoints가 계산된 전역 변수로 가정합니다.
    global midpoints

    pc_data = pc2.read_points(msg, skip_nans=True, field_names=("x", "y", "z"))
    pc_array = np.array(list(pc_data))

    left_lane = []
    right_lane = []
    for point in pc_array:
        x, y, z = point
        distance = np.sqrt(x**2 + y**2 + z**2)
        if y > 1:
            left_lane.append(point)
        else:
            right_lane.append(point)

    left_lane = np.array(left_lane)
    right_lane = np.array(right_lane)

    midpoints = find_centerline_path(left_lane, right_lane)

    header = std_msgs.msg.Header()
    header.stamp = rospy.Time.now()
    header.frame_id = msg.header.frame_id

    fields = [
        pc2.PointField('x', 0, pc2.PointField.FLOAT32, 1),
        pc2.PointField('y', 4, pc2.PointField.FLOAT32, 1),
        pc2.PointField('z', 8, pc2.PointField.FLOAT32, 1),
    ]

    # 중앙선(centerline)을 포인트 클라우드 데이터로 변환합니다.
    points = [(point[0], point[1], point[2]) for point in midpoints]

    # 추가적인 z값 (예: 0.0)을 모든 포인트에 추가합니다.
    points_with_z = [(point[0], point[1], 0.0) for point in points]

    # 포인트 클라우드 메시지를 생성합니다.
    pc_msg = pc2.create_cloud(header, fields, points_with_z)

    # 포인트 클라우드 메시지를 발행합니다.
    pub.publish(pc_msg)

def listener():
    rospy.init_node('pointcloud_listener', anonymous=True)
    rospy.Subscriber('/object_centroids', PointCloud2, pointcloud_callback)
    rospy.spin()

if __name__ == '__main__':
    # Define the publisher globally
    pub = rospy.Publisher('/path_planning', PointCloud2, queue_size=10)

    # midpoints를 빈 배열로 초기화합니다.
    midpoints = []

    listener()
