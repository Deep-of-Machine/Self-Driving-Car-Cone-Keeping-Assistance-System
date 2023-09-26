#!/usr/bin/env python3

import numpy as np
import rospy
from sensor_msgs.msg import PointCloud2
import sensor_msgs.point_cloud2 as pc2
from std_msgs.msg import Float64, Int16

class StanleyController:
    def __init__(self):
        self.midpoints = None
        self.k = 0.3      # 상수 k (튜닝이 필요) 원돌이 0.3
        self.filtered_yaw = 0.0  # 초기화
        self.gps_speed = 0.0  # 초기화

        self.vehicle_pos = np.array([0, 0])
        self.rate = rospy.Rate(20)
        self.sub_ya = rospy.Subscriber('/filtered/imu/yaw', Float64, self.imu_callback)
        self.sub_path = rospy.Subscriber('/path_planning', PointCloud2, self.path_callback)
        self.sub_gps_speed = rospy.Subscriber('/gps_speed', Float64, self.gps_speed_callback)
        self.pub = rospy.Publisher('/steering_angle', Int16, queue_size=1)
        self.pub_speed = rospy.Publisher('/motor', Int16, queue_size=1)  # 감속 속도 publisher

        
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
        
        # distances = np.linalg.norm(self.midpoints[:, :2] - self.vehicle_pos, axis=1)
        # closest_idx = np.argmin(distances)
        # farthest_idx = np.argmax(distances)
        # closest_point = self.midpoints[closest_idx]
        # farthest_point = self.midpoints[farthest_idx]
        # delta_y = farthest_point[1] - closest_point[1]
        # delta_x = farthest_point[0] - closest_point[0]
        # path_yaw = 0.7 * np.arctan2(delta_y, delta_x)


        # Use broadcasting and vectorization for efficient computation
        distances = np.linalg.norm(self.midpoints[:, :2] - self.vehicle_pos, axis=1)
        sorted_indices = np.argsort(distances)
        closest_idx = sorted_indices[0]
        third_closest_idx = sorted_indices[-1]  # 3번째로 가까운 점의 인덱스
        closest_point = self.midpoints[closest_idx]
        third_closest_point = self.midpoints[third_closest_idx]  # 3번째로 가까운 점
        delta_y = third_closest_point[1] - closest_point[1]
        delta_x = third_closest_point[0] - closest_point[0]
        path_yaw = np.arctan2(delta_y, delta_x)
        # yaw = self.ya
        if path_yaw >= np.pi/8 and path_yaw <= np.pi*7/8:
            # print("감속")
            self.pub_speed.publish(Int16(10))  # 속도를 30으로 감속
        else:
            self.pub_speed.publish(Int16(30))
            # print("가속")

        print('앞', path_yaw)
        idx = closest_idx  # Already computed
        lookahead_point = self.midpoints[idx]
        x_error = lookahead_point[1]

        print('err', x_error)
        if self.gps_speed > 1 and self.gps_speed < 30:
            speed_for_calculation = self.gps_speed
        else:
            speed_for_calculation = 1
        # print('뒤', (np.arctan2(self.k * x_error, speed_for_calculation)))
        steering_angle = np.arctan2(self.k * x_error, speed_for_calculation) #path_yaw+

        max_steering_angle = np.radians(25)
        steering_angle = np.clip(steering_angle, -max_steering_angle, max_steering_angle)

        mapped_steering_angle = np.interp(steering_angle, [-max_steering_angle, max_steering_angle], [6.25, 78]) #42.27
        # self.pub.publish(Int16(data=int(555)))
        self.pub.publish(Int16(data=int(42)))  # std_msgs/Int16 형식에 맞게 수정
        print(mapped_steering_angle)
        #self.rate.sleep()   


if __name__ == '__main__':
    rospy.init_node('stanley_controller')
    
    controller = StanleyController()
    rospy.spin()