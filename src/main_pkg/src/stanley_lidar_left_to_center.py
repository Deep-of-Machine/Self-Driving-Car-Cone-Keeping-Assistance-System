#!/usr/bin/env python3

import numpy as np
import rospy
from sensor_msgs.msg import PointCloud2
import sensor_msgs.point_cloud2 as pc2
from std_msgs.msg import Float64, Int16

class StanleyController:
    def __init__(self):
        self.midpoints = None
        self.k = 0.3      # 상수 k (튜닝이 필요) 원돌이 0.3 / 0.8요 - 0.7 추천 / 0.5요 - 0.5
        self.filtered_yaw = 0.0  # 초기화
        self.gps_speed = 0.0  # 초기화
        self.voltage_brake_count = 0


        self.vehicle_pos = np.array([0, 0])
        # self.rate = rospy.Rate(20)
        self.sub_ya = rospy.Subscriber('/filtered/imu/yaw', Float64, self.imu_callback)
        self.sub_path = rospy.Subscriber('/new_right_lane', PointCloud2, self.path_callback)
        self.sub_gps_speed = rospy.Subscriber('/gps_speed', Float64, self.gps_speed_callback)
        self.pub = rospy.Publisher('/steering_angle', Int16, queue_size=1)
        self.pub_speed = rospy.Publisher('/motor', Int16, queue_size=1)  # 감속 속도 publisher

        
    def path_callback(self, msg):
        self.midpoints = np.array(list(pc2.read_points(msg, skip_nans=True, field_names=("x", "y", "z"))))
        self.control()

    def gps_speed_callback(self, msg):
        # GPS 속도 데이터를 사용
        self.gps_speed = msg.data

    def calculate_curvature(self, path_yaw):
        # 곡률은 연속된 두 포인트 간의 각도 차이로 추정합니다.
        curvature = abs(path_yaw)

        # 최대 곡률을 np.pi /2로 설정
        curvature = min(curvature ,np.pi /2)
        return curvature

    def imu_callback(self, msg):
        # GPS 속도 데이터를 사용
        self.ya = msg.data

    def voltage_brake(self):
        print("회생제동 ON !!!!!")

    def control(self):
        if self.midpoints is None:
            return
        
        distances = np.linalg.norm(self.midpoints[:, :2] - self.vehicle_pos, axis=1)
        sorted_indices = np.argsort(distances)

        two_last_idx = sorted_indices[-1]
        last_closest_idx = sorted_indices[-2]  # 3번째로 가까운 점의 인덱스
        two_last_point = self.midpoints[two_last_idx]
        last_closest_point = self.midpoints[last_closest_idx]  # 3번째로 가까운 점
        delta_y = last_closest_point[1] - two_last_point[1]
        delta_x = last_closest_point[0] - two_last_point[0]
        speed_yaw = np.abs(np.arctan2(delta_y, delta_x))
        print(speed_yaw)
        # yaw = self.ya
        if speed_yaw < 2.75:
            self.pub_speed.publish(Int16(10))  # 속도를 30으로 감속
            print('감속')
            self.voltage_brake_count += 1

        else:
            self.pub_speed.publish(Int16(30))
            print("가속")
            self.voltage_brake_count = 0


        if 5 > self.voltage_brake_count > 3:
            self.voltage_brake()

        closest_idx = sorted_indices[0]
        last_closest_idx = sorted_indices[-1]  # 3번째로 가까운 점의 인덱스
        closest_point = self.midpoints[closest_idx]
        last_closest_point = self.midpoints[last_closest_idx]  # 3번째로 가까운 점
        delta_y = last_closest_point[1] - closest_point[1]
        delta_x = last_closest_point[0] - closest_point[0]
        path_yaw = np.arctan2(delta_y, delta_x)
        path_yaw = path_yaw * 0.5

                # print('앞', path_yaw)
        idx = closest_idx  # Already computed
        lookahead_point = self.midpoints[sorted_indices[1]]
        # print(lookahead_point)
        x_error = lookahead_point[1]

        # print('err', x_error)
        if self.gps_speed > 1 and self.gps_speed < 30:
            speed_for_calculation = self.gps_speed
            # print('gps_callback')
        else:
            speed_for_calculation = 1

        curvature = self.calculate_curvature(path_yaw)

        # 선형 보간을 사용하여 k 값을 동적으로 조정
        k_straight = 0.05  # 직선 코스용 k 값
        k_curve = 0.5  # 곡선 코스용 k 값

        # 곡률의 기준값
        curvature_straight = 0.0
        curvature_curve = np.pi / 2

        # 선형 보간
        self.k = np.interp(curvature, [curvature_straight, curvature_curve], [k_straight, k_curve])

        # print('뒤', (np.arctan2(self.k * x_error, speed_for_calculation)))
        steering_angle= path_yaw + np.arctan2(self.k * x_error, speed_for_calculation) #path_yaw+

        max_steering_angle = np.radians(22.2)
        steering_angle = np.clip(steering_angle, -max_steering_angle, max_steering_angle)

        mapped_steering_angle = np.interp(steering_angle, [-max_steering_angle, max_steering_angle], [6.25, 78]) #42.27
        # self.pub.publish(Int16(data=int(555)))
        # print(mapped_steering_angle)
        self.pub.publish(Int16(data=int(mapped_steering_angle)))  # std_msgs/Int16 형식에 맞게 수정
        # print(mapped_steering_angle)
        # self.rate.sleep()   


if __name__ == '__main__':
    rospy.init_node('stanley_controller')
    
    controller = StanleyController()   













    
    rospy.spin()