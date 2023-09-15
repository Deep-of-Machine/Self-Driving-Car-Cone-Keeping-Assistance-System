#!/usr/bin/env python3

import numpy as np
import rospy
from std_msgs.msg import Float64, String
from pyproj import Proj
from sensor_msgs.msg import NavSatFix  # For ublox

class StanleyController:
    def __init__(self):
        self.k = 0.3
        self.gps_speed = 0.0
        self.rate = rospy.Rate(20)
        
        self.proj = Proj(proj='utm', zone=52, ellps='WGS84')

        # Separate initial latitudes and longitudes
        initial_latitudes = [37.7749, 37.7750]  # Replace these with your values
        initial_longitudes = [-122.4194, -122.4195]  # Replace these with your values
        
        self.midpoints = [self.proj(lon, lat) for lat, lon in zip(initial_latitudes, initial_longitudes)]
        self.midpoints = np.array(self.midpoints)
        
        self.vehicle_pos = np.zeros(2)
        
        self.sub_gps_speed = rospy.Subscriber('/gps_speed', Float64, self.gps_speed_callback)
        self.sub_ublox_gps = rospy.Subscriber('/ublox_gps', NavSatFix, self.ublox_gps_callback)  # Replace topic name
        self.pub = rospy.Publisher('/steering_angle', Float64, queue_size=10)

    def gps_speed_callback(self, msg):
        self.gps_speed = msg.data

    def ublox_gps_callback(self, msg):
        self.vehicle_pos = np.array(self.proj(msg.longitude, msg.latitude))
        
    def control(self):
        if len(self.midpoints) == 0:
            return

        distances = np.linalg.norm(self.midpoints - self.vehicle_pos, axis=1)
        closest_idx = np.argmin(distances)

        lookahead_point = self.midpoints[closest_idx]

        # Calculate path_yaw
        path_yaw = np.arctan2(lookahead_point[1] - self.vehicle_pos[1], lookahead_point[0] - self.vehicle_pos[0])

        cross_track_error = np.linalg.norm(lookahead_point - self.vehicle_pos)

        steering_angle = path_yaw + np.arctan2(self.k * cross_track_error, self.gps_speed)

        max_steering_angle = np.radians(25)
        steering_angle = np.clip(steering_angle, -max_steering_angle, max_steering_angle)

        mapped_steering_angle = np.interp(steering_angle, [-max_steering_angle, max_steering_angle], [86, 1024])

        self.pub.publish(mapped_steering_angle)
        self.rate.sleep()

if __name__ == '__main__':
    rospy.init_node('stanley_controller')
    controller = StanleyController()
    while not rospy.is_shutdown():
        controller.control()
