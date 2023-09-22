#!/usr/bin/env python3

import numpy as np
import rospy
from sensor_msgs.msg import PointCloud2
import sensor_msgs.point_cloud2 as pc2
from std_msgs.msg import Float64, Int16

class StanleyController:
    def __init__(self):
        self.midpoints = None
        self.sub_vehicle_yaw = 0.0  # 초기화
        self.rate = rospy.Rate(20)

        self.pub_steering = rospy.Publisher('/steering_angle', Int16, queue_size=1)
        self.pub_speed = rospy.Publisher('/decelerate_speed', Int16, queue_size=1)  # 감속 속도 publisher
        self.sub_vehicle_yaw = rospy.Subscriber('/filtered/imu/yaw', Float64, self.vehicle_yaw_callback)


    def path_callback(self, msg):
        self.midpoints = np.array(list(pc2.read_points(msg, skip_nans=True, field_names=("x", "y", "z"))))
        self.control()
    
    def vehicle_yaw_callback(self, msg):
        self.sub_vehicle_yaw = msg.data

        
    def control(self):
        if self.midpoints is None:
            return

        steering_angle = self.sub_vehicle_yaw

        max_steering_angle = np.radians(25)
        steering_angle = np.clip(steering_angle, -max_steering_angle, max_steering_angle)

        mapped_steering_angle = np.interp(steering_angle, [-max_steering_angle, max_steering_angle], [0, 78]) #24 1023
        self.pub.publish(Int16(data=int(mapped_steering_angle)))  # std_msgs/Int16 형식에 맞게 수정
        print(mapped_steering_angle)


        self.rate.sleep()

if __name__ == '__main__':
    rospy.init_node('stanley_controller')
    controller = StanleyController()
    rospy.spin()
 