#!/usr/bin/env python3

import rospy
import math
import numpy as np
from sensor_msgs.msg import Imu, NavSatFix
from std_msgs.msg import Float64
from pyproj import Proj

class StanleyControlNode:
    def __init__(self):
        self.imu_yaw = 0.0
        self.gps_lat = None
        self.gps_lon = None
        self.v = 5.0  # 초기 속도
        self.max_steering_angle = 0.35  # 라디안, 최대 조향각
        self.k = 0.5  # Stanley controller tuning parameter
        self.path_x = [ 37.3014406, 37.301440299999996, 37.301438, 37.3014327, 37.3014248, 37.3014149, 37.3014033, 37.3013897, 37.3013747, 37.3013596, 37.3013443, 37.3013323, 37.3013203, 37.3013068, 37.3012922, 37.3012763, 37.3012619, 37.301246899999995, 37.301229899999996, 37.3012114, 37.3011921, 37.3011732, 37.3011541, 37.3011377, 37.301128999999996, 37.3011228, 37.3011149, 37.301104599999995, 37.3010884, 37.3010704, 37.3010532, 37.3010351, 37.3010174, 37.3009993, 37.300982, 37.300971499999996, 37.3009699]
        self.path_y = [ 126.8347268, 126.8347266, 126.8347251, 126.83472069999999, 126.8347129, 126.83470279999999, 126.83469149999999, 126.8346796, 126.8346684, 126.8346605, 126.83466, 126.83466659999999, 126.8346744, 126.8346838, 126.83469269999999, 126.83469299999999, 126.8346859, 126.834678, 126.8346711, 126.83466259999999, 126.8346531, 126.8346421, 126.83463139999999, 126.834616, 126.8345935, 126.83456969999999, 126.8345459, 126.8345236, 126.83450939999999, 126.83450389999999, 126.83449429999999, 126.8344826, 126.8344707, 126.83445979999999, 126.83444879999999, 126.8344422, 126.8344412]


        # UTM 변환을 위한 객체 (Zone 52로 변경)
        self.utm_converter = Proj(proj="utm", zone=52, ellps="WGS84")

        rospy.init_node('stanley_control_node', anonymous=True)
        rospy.Subscriber("/filtered/imu/yaw", Imu, self.imu_callback)
        rospy.Subscriber("/ublox_gps/fix", NavSatFix, self.gps_callback)
        rospy.Subscriber("/gps_speed", Float64, self.gps_speed_callback)
        self.pub = rospy.Publisher("/steering_angle", Float64, queue_size=10)

    def imu_callback(self, data):
        self.imu_yaw = data.data

    def gps_speed_callback(self, data):
        self.v = 5 # data.data

    def gps_callback(self, data):
        self.gps_lat = data.latitude
        self.gps_lon = data.longitude

    def get_cartesian_coords(self, lat, lon):
        x, y = self.utm_converter(lon, lat)
        return x, y

    def stanley_control(self, x, y, yaw, v, cx, cy):
        dx = [x - icx for icx in cx]
        dy = [y - icy for icy in cy]
        d = np.hypot(dx, dy)

        # 차량 헤딩을 고려하여 앞에 있는 점만 고려
        angles = [math.atan2(dy[i], dx[i]) for i in range(len(dx))]
        angles = np.array(angles) - yaw
        angles = np.abs(((angles + np.pi) % (2 * np.pi)) - np.pi)  # Normalize angles to -pi to pi
        forward_indices = np.where(angles <= np.pi / 2)[0]
        
        if len(forward_indices) == 0:
            target_idx = len(cx) - 1  # Fallback: use the last point if no point is ahead.
        else:
            d_forward = d[forward_indices]
            lookahead_distance = np.abs(v)
            target_idx = forward_indices[np.argmin(np.abs(d_forward - lookahead_distance))]

        target_theta = math.atan2(cy[target_idx] - y, cx[target_idx] - x)
        theta_e = target_theta - yaw

        delta = theta_e + math.atan2(self.k * d[target_idx], v)
        return delta, target_idx

    def run(self):
        rate = rospy.Rate(10)
        while not rospy.is_shutdown():
            if self.gps_lat is not None and self.gps_lon is not None:
                x, y = self.get_cartesian_coords(self.gps_lat, self.gps_lon)
                self.path_x, self.path_y = self.get_cartesian_coords(self.path_x, self.path_y)
                delta, _ = self.stanley_control(x, y, self.imu_yaw, self.v, self.path_x, self.path_y)
                print(delta)
                delta = max(min(delta, self.max_steering_angle), -self.max_steering_angle)
                
                self.pub.publish(delta)
            rate.sleep()

if __name__ == '__main__':
    try:
        node = StanleyControlNode()
        node.run()
    except rospy.ROSInterruptException:
        pass