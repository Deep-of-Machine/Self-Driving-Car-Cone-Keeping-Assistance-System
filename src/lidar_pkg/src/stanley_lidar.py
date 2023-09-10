#!/usr/bin/env python3

import numpy as np
import rospy
from sensor_msgs.msg import PointCloud2
import sensor_msgs.point_cloud2 as pc2
from std_msgs.msg import Float64
from sensor_msgs.msg import Imu

class StanleyController:
    def __init__(self):
        self.midpoints = None
        self.k = 0.1  # 상수 k (튜닝이 필요)

        self.imu_yaw = 0.0  # 초기화
        self.filtered_yaw = 0.0  # 초기화
        self.gps_speed = 0.0  # 초기화

        self.sub_path = rospy.Subscriber('/path_planning', PointCloud2, self.path_callback)
        self.sub_imu = rospy.Subscriber('/filtered/imu/yaw', Imu, self.imu_callback)
        self.sub_gps_speed = rospy.Subscriber('/gps_speed', Float64, self.gps_speed_callback)
        self.pub = rospy.Publisher('/steering_angle', Float64, queue_size=10)
        
    def path_callback(self, msg):
        self.midpoints = np.array(list(pc2.read_points(msg, skip_nans=True, field_names=("x", "y", "z"))))
        self.control()

    def imu_callback(self, msg):
        # IMU 데이터로부터 yaw 값을 추출 (단위: 라디안)
        self.imu_yaw = msg.data  # IMU 메시지에서 yaw 값을 추출합니다.

    def gps_speed_callback(self, msg):
        # GPS 속도 데이터를 사용
        self.gps_speed = msg.data

    def control(self):
        if self.midpoints is None:
            return

        # Find the closest and farthest points to the vehicle
        vehicle_pos = np.array([0, 0])
        distances = np.linalg.norm(self.midpoints[:, :2] - vehicle_pos, axis=1)
        closest_idx = np.argmin(distances)
        farthest_idx = np.argmax(distances)

        closest_point = self.midpoints[closest_idx]
        farthest_point = self.midpoints[farthest_idx]

        # Calculate the slope of the line connecting the closest and farthest points
        delta_y = farthest_point[1] - closest_point[1]
        delta_x = farthest_point[0] - closest_point[0]
        path_yaw = np.arctan2(delta_y, delta_x)  # 경로 방향을 아크탄젠트로 계산합니다.

        # Find the point in the path that's closest to the vehicle within the lookahead distance
        distances = np.linalg.norm(self.midpoints[:, :2] - vehicle_pos, axis=1)
        idx = np.argmin(distances)
        lookahead_point = self.midpoints[idx]

        # Calculate the error in the x-direction (종방향 오차 계산)
        x_error = lookahead_point[1] - vehicle_pos[0]

        # Calculate the heading error (헤딩 오차 계산)
        heading_error = path_yaw - self.imu_yaw  # 경로 방향과 IMU 방향의 차이를 계산합니다.

        # Calculate the desired steering angle using Stanley control formula
        if self.gps_speed > 2 and self.gps_speed < 10:
            steering_angle = heading_error + np.arctan2(self.k * x_error, self.gps_speed)
        else:
            self.gps_speed = 1
            steering_angle = heading_error + np.arctan2(self.k * x_error, self.gps_speed)

        # Apply saturation limits to the steering angle
        max_steering_angle = np.radians(50)  # 최대 조향각을 50도로 설정
        steering_angle = np.clip(steering_angle, -max_steering_angle, max_steering_angle)

         # Map the steering_angle from -50 to 50 degrees to 0 to 7
        mapped_steering_angle = np.interp(steering_angle, [-max_steering_angle, max_steering_angle], [0, 1024])

        self.pub.publish(mapped_steering_angle)
        print(f"Steering Angle: {mapped_steering_angle} (mapped) degrees")


if __name__ == '__main__':
    rospy.init_node('stanley_controller')
    controller = StanleyController()
    rospy.spin()