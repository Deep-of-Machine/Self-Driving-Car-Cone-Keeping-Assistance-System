#!/usr/bin/env python3

import numpy as np
import rospy
from sensor_msgs.msg import PointCloud2
import sensor_msgs.point_cloud2 as pc2
from std_msgs.msg import Float64
import socket  # 소켓 라이브러리 추가

class StanleyController:
    def __init__(self):
        self.midpoints = None
        self.lookahead_distance = 2.0  # 임의의 값
        self.max_steering_angle = np.radians(20)  # 최대 조향각
        self.k = 0.5  # Control gain
        self.prev_steering_angle = 0.0  # 이전 조향 각도
        self.rate_limit = np.radians(5)  # 5도/초

        self.sub = rospy.Subscriber('/path_planning', PointCloud2, self.path_callback)
        self.pub = rospy.Publisher('/steering_angle', Float64, queue_size=10)

        # 소켓 생성 및 설정
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.client_socket.connect(('라즈베리파이_아이피', 포트번호))  # 라즈베리파이 IP와 포트를 입력
        
    def path_callback(self, msg):
        self.midpoints = np.array(list(pc2.read_points(msg, skip_nans=True, field_names=("x", "y", "z"))))
        self.control()

    def control(self):
        if self.midpoints is None:
            return

        # Vehicle position (assuming it's at (0,0) for simplicity)
        vehicle_pos = np.array([0, 0])

        # Find the point in the path that's closest to the vehicle within the lookahead distance
        distances = np.linalg.norm(self.midpoints[:, :2] - vehicle_pos, axis=1)
        idx = np.argmin(distances)
        lookahead_point = self.midpoints[idx]

        # Calculate the Cross-Track Error with sign
        vector_to_lookahead = lookahead_point[:2] - vehicle_pos
        cte = np.linalg.norm(vector_to_lookahead)  # magnitude
        if np.cross(vector_to_lookahead, np.array([1, 0])) < 0:
            cte *= -1  # add sign based on side

        # Calculate the heading error
        path_heading = np.arctan2(lookahead_point[1], lookahead_point[0])
        heading_error = path_heading

        # Calculate steering angle using full Stanley controller formula
        steering_angle = heading_error + np.arctan2(self.k * cte, 1)

        # Apply rate limiting
        delta_angle = steering_angle - self.prev_steering_angle
        delta_angle = np.clip(delta_angle, -self.rate_limit, self.rate_limit)
        steering_angle = self.prev_steering_angle + delta_angle

        # Clamp the steering angle to the maximum value
        steering_angle = np.clip(steering_angle, -self.max_steering_angle, self.max_steering_angle)

        # Map the steering_angle from -50 to 50 degrees to 0 to 7
        mapped_steering_angle = np.interp(steering_angle, [-self.max_steering_angle, self.max_steering_angle], [0, 78])

        # 소켓을 통해 라즈베리파이로 mapped_steering_angle 전송
        self.client_socket.send(str(mapped_steering_angle).encode('utf-8'))

        self.prev_steering_angle = steering_angle  # Update previous angle

        self.pub.publish(steering_angle)
        print(f"Steering Angle: {np.degrees(steering_angle)} degrees")
        print(f"Steering Angle_mm: {mapped_steering_angle} mm")

if __name__ == '__main__':
    rospy.init_node('stanley_controller')
    controller = StanleyController()
    rospy.spin()
