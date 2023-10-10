#!/usr/bin/env python3

import numpy as np
import rospy
from sensor_msgs.msg import PointCloud2
import sensor_msgs.point_cloud2 as pc2
from std_msgs.msg import Float64
import socket  # 소켓 라이브러리 추가

class StanleyController:
    def __init__(self):
        self.sub = rospy.Subscriber('/filtered/imu/yaw', PointCloud2, self.path_callback)
        self.pub = rospy.Publisher('/steering_angle', Float64, queue_size=10)
        
    def path_callback(self, msg):
        self.midpoints = np.array(list(pc2.read_points(msg, skip_nans=True, field_names=("x", "y", "z"))))
        self.control()

    def control(self):
        self.pub.publish(angle)

if __name__ == '__main__':
    rospy.init_node('imu_steering')
    controller = StanleyController()
    rospy.spin()
