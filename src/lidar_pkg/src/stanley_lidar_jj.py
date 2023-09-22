#!/usr/bin/env python3

import numpy as np
import rospy
from sensor_msgs.msg import PointCloud2
import sensor_msgs.point_cloud2 as pc2
from std_msgs.msg import Float64, Int16

class StanleyController:
    def __init__(self):
        self.midpoints = None
        self.k = 0.1      # 상수 k (튜닝이 필요)
        self.filtered_yaw = 0.0  # 초기화
        self.gps_speed = 0.0  # 초기화

        self.vehicle_pos = np.array([0, 0])
        self.rate = rospy.Rate(20)
        self.sub_path = rospy.Subscriber('/path_planning', PointCloud2, self.path_callback)
        self.sub_gps_speed = rospy.Subscriber('/gps_speed', Float64, self.gps_speed_callback)
        self.pub_steering = rospy.Publisher('/steering_angle', Int16, queue_size=1)
        self.pub_speed = rospy.Publisher('/decelerate_speed', Int16, queue_size=1)  # 감속 속도 publisher

        
    def path_callback(self, msg):
        self.midpoints = np.array(list(pc2.read_points(msg, skip_nans=True, field_names=("x", "y", "z"))))
        self.control()

    def gps_speed_callback(self, msg):
        self.gps_speed = msg.data
    

    def control(self):
        if self.midpoints is None:
            return

        # 감속 조건 판단
        fifth_point = self.midpoints[4]
        last_point = self.midpoints[-1]
        slope = np.arctan2(last_point[1] - fifth_point[1], last_point[0] - fifth_point[0])
        if slope >= np.pi/8 and slope <= np.pi*7/8:
            # 감속 코드
            print("감속")
            self.pub_speed.publish(Int16(30))  # 속도를 30으로 감속
        else:
            self.pub_speed.publish(Int16(255))
            print("가속")
        # print(slope)
        # Use broadcasting and vectorization for efficient computation
        

        # steering_angle = slope + np.arctan2(self.k * x_error, speed_for_calculation)

        # max_steering_angle = np.radians(25)
        # steering_angle = np.clip(steering_angle, -max_steering_angle, max_steering_angle)

        # mapped_steering_angle = np.interp(steering_angle, [-max_steering_angle, max_steering_angle], [84, 1023])
        # self.pub_steering.publish(Int16(data=int(mapped_steering_angle)))

        self.rate.sleep()

if __name__ == '__main__':
    rospy.init_node('stanley_controller')
    controller = StanleyController()
    rospy.spin()
 