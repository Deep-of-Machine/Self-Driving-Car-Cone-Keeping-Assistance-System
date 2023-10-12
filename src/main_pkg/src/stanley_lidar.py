#!/usr/bin/env python3

import numpy as np
import rospy
from sensor_msgs.msg import PointCloud2
import sensor_msgs.point_cloud2 as pc2
from std_msgs.msg import Float64, Int16

class StanleyController:
    def __init__(self):
        self.midpoints = None
        self.k = 0.6      # 상수 k (튜닝이 필요) 원돌이 0.3 / 0.8요 - 0.7 추천 / 0.5요 - 0.5
        self.filtered_yaw = 0.0  # 초기화
        self.gps_speed = 0.0  # 초기화
        self.voltage_brake_count = 0
        self.speed = 3
        self.flag = 0
        self.fast_change = 11
        self.prev_value = None

        self.vehicle_pos = np.array([0, 0])
        self.sub_ya = rospy.Subscriber('/filtered/imu/yaw', Float64, self.imu_callback)
        self.sub_path = rospy.Subscriber('/new_right_lane', PointCloud2, self.path_callback)
        self.sub_gps_speed = rospy.Subscriber('/gps_speed', Float64, self.gps_speed_callback)
        self.pub = rospy.Publisher('/steering_angle', Int16, queue_size=1)
        self.pub_speed = rospy.Publisher('/motor', Int16, queue_size=1)  # 감속 속도 publisher

        self.pub_brake = rospy.Publisher('/voltage_brake', Int16, queue_size=1)  


        
    def path_callback(self, msg):
        self.midpoints = np.array(list(pc2.read_points(msg, skip_nans=True, field_names=("x", "y", "z"))))
        self.control()

    def gps_speed_callback(self, msg):
        # GPS 속도 데이터를 사용
        self.gps_speed = msg.data

    def imu_callback(self, msg):
        # GPS 속도 데이터를 사용
        self.ya = msg.data


    def control(self):
        if self.midpoints is None:
            return

        distances = np.linalg.norm(self.midpoints[:, :2] - self.vehicle_pos, axis=1)
        sorted_indices = np.argsort(distances)
        speed_cloest = sorted_indices[0]
        third_speed_idx = sorted_indices[-1]  # 3번째로 가까운 점의 인덱스
        speed_cpoint = self.midpoints[speed_cloest]
        speed_fpoint = self.midpoints[third_speed_idx]  # 3번째로 가까운 점
        delta_y = speed_fpoint[1] - speed_cpoint[1]
        delta_x = speed_fpoint[0] - speed_cpoint[0]
        speed_yaw = np.arctan2(delta_y, delta_x)
        speed_yaw = speed_yaw


        print("speed_yaw : ", speed_yaw)

        closest_idx = sorted_indices[0]
        third_closest_idx = sorted_indices[2]  # 3번째로 가까운 점의 인덱스
        closest_point = self.midpoints[closest_idx]
        third_closest_point = self.midpoints[third_closest_idx]  # 3번째로 가까운 점
        delta_y = third_closest_point[1] - closest_point[1]
        delta_x = third_closest_point[0] - closest_point[0]
        path_yaw = np.arctan2(delta_y, delta_x)

        print("path_yaw : ", path_yaw)

        if self.flag > 0:
            self.pub_speed.publish(Int16(int(35)))  # 속도를 30으로 감속
            print('회생 후 느리게')
            self.flag -= 1
            self.voltage_brake_count -= 1000
        else:
            if np.abs(speed_yaw) < 0.3:
                self.fast_change += 1
                if self.fast_change > 10:
                    self.pub_speed.publish(Int16(int(45)))  # 속도를 30으로 감속
                    print('빠름')
                    self.voltage_brake_count = 0
                    self.flag -= 1
                else:
                    self.pub_speed.publish(Int16(int(35)))
                    print("느림")
                    self.voltage_brake_count += 1
                    self.flag -= 1
                    
                    current_value = speed_yaw

                    if self.prev_value is not None:
                        if (self.prev_value > 0 and current_value < 0) or (self.prev_value < 0 and current_value > 0):
                            self.voltage_brake_count = 8

                    self.prev_value = current_value
                    
            else:
                self.pub_speed.publish(Int16(int(45)))
                print("느림")
                self.voltage_brake_count += 1
                self.flag -= 1
                self.fast_change =0


        if 9 > self.voltage_brake_count > 7:
            self.pub_brake.publish(1)
            print("회생제동 ON")
            self.flag = 30
        else:
            self.pub_brake.publish(0)

        # print('앞', path_yaw)
        lookahead_point = self.midpoints[closest_idx]
        x_error = lookahead_point[1]

        # print('err', x_error)
        # if self.gps_speed > 1 and self.gps_speed < 30:
        #     speed_for_calculation = self.gps_speed
        #     # print('gps_callback')
        # else:
        #     speed_for_calculation = 5

        speed_for_calculation = 1

        # print('뒤', (np.arctan2(self.k * x_error, speed_for_calculation)))

        # 선형 보간
        self.k = np.interp(np.abs(path_yaw), [0, np.pi/2], [0.03, 2.5])

        path_yaw = path_yaw * 0.85

        steering_angle = path_yaw + np.arctan2(self.k * x_error, speed_for_calculation) #path_yaw+

        max_steering_angle = np.radians(22.2)
        steering_angle = np.clip(steering_angle, -max_steering_angle, max_steering_angle)

        mapped_steering_angle = np.interp(steering_angle, [-max_steering_angle, max_steering_angle], [6.54, 78]) #42.27
        # self.pub.publish(Int16(data=int(555)))
        # print(mapped_steering_angle)
        self.pub.publish(Int16(data=int(mapped_steering_angle)))  # std_msgs/Int16 형식에 맞게 수정
        print("steering_angle: ", int((np.degrees(steering_angle))))


if __name__ == '__main__':
    rospy.init_node('stanley_controller')
    
    controller = StanleyController()
    rospy.spin()