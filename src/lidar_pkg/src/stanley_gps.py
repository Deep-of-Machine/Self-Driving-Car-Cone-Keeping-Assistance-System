#!/usr/bin/env python3

from pyproj import Proj
import numpy as np
import rospy
from sensor_msgs.msg import NavSatFix
from std_msgs.msg import Float64

class StanleyController:
    def __init__(self):
        self.k = 0.1
        self.filtered_yaw = 0.0
        self.gps_speed = 0.0
        self.x = 0
        self.y = 0
        self.utm_converter = Proj(proj="utm", zone=52, ellps="WGS84")
        self.path_x = [...]  # Latitude values from your original code
        self.path_y = [...]  # Longitude values from your original code
        self.path_latlon = np.column_stack((self.path_x, self.path_y))
        self.midpoints = np.array([self.utm_converter(x, y) for x, y in self.path_latlon])
        self.sub_xy = rospy.Subscriber("/ublox_gps/fix", NavSatFix, self.gps_callback)
        self.sub_yaw = rospy.Subscriber('/filtered/imu/yaw', Float64, self.imu_callback)
        self.sub_gps_speed = rospy.Subscriber('/gps_speed', Float64, self.gps_speed_callback)
        self.pub = rospy.Publisher('/steering_angle', Float64, queue_size=10)

    def imu_callback(self, data):
        self.filtered_yaw = data.data

    def gps_callback(self, data):
        self.x, self.y = self.utm_converter(data.latitude, data.longitude)

    def gps_speed_callback(self, msg):
        self.gps_speed = msg.data

    def path_yaw_calculation(self, idx):
        dx = self.midpoints[idx + 1][0] - self.midpoints[idx][0]
        dy = self.midpoints[idx + 1][1] - self.midpoints[idx][1]
        return np.arctan2(dy, dx)

    def control(self):
        if self.midpoints is None:
            return

        # Calculate path_yaw
        distances = np.linalg.norm(self.midpoints - np.array([self.x, self.y]), axis=1)
        closest_idx = np.argmin(distances)

        # Consider vehicle's current yaw to choose lookahead point
        path_yaw = self.path_yaw_calculation(closest_idx)
        angle_diff = np.abs(self.filtered_yaw - path_yaw)
        
        if angle_diff > np.pi / 2:  # 90 degrees
            closest_idx += 1  # Move to the next closest point

        if closest_idx < len(self.midpoints) - 1:
            path_yaw = self.path_yaw_calculation(closest_idx)
        else:
            path_yaw = self.path_yaw_calculation(closest_idx - 1)

        # Heading error
        heading_error = path_yaw - self.filtered_yaw

        # Calculate steering angle
        x_error = self.midpoints[closest_idx][0] - self.x
        if self.gps_speed > 2 and self.gps_speed < 30:
            steering_angle = heading_error + np.arctan2(self.k * x_error, self.gps_speed)
        else:
            steering_angle = heading_error + np.arctan2(self.k * x_error, 1)

        # Apply saturation limits
        max_steering_angle = np.radians(25)
        steering_angle = np.clip(steering_angle, -max_steering_angle, max_steering_angle)

        # Publish the results
        mapped_steering_angle = np.interp(steering_angle, [-max_steering_angle, max_steering_angle], [0, 7])
        self.pub.publish(mapped_steering_angle)

if __name__ == '__main__':
    rospy.init_node('stanley_controller')
    controller = StanleyController()
    rospy.spin()

