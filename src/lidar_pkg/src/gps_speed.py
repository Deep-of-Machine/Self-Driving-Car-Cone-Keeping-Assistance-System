#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import NavSatFix
from std_msgs.msg import Float64
import math
from pyproj import Proj

class UTMToSpeed:
    def __init__(self):
        rospy.init_node('utm_to_speed', anonymous=True)
        self.prev_x = None
        self.prev_y = None
        self.prev_time = None
        self.speed_pub = rospy.Publisher('gps_speed', Float64, queue_size=10)
        rospy.Subscriber('/ublox_gps/fix', NavSatFix, self.utm_callback)
        rospy.spin()

    def utm_callback(self, data):
        # UTM 좌표계 정의 (Zone 52, WGS84)
        utm_proj = Proj(proj='utm', zone=52, ellps='WGS84')
        
        latitude = data.latitude
        longitude = data.longitude

        current_x, current_y = utm_proj(float(longitude), float(latitude))
        current_time = data.header.stamp

        if self.prev_x is not None and self.prev_y is not None and self.prev_time is not None:
            delta_x = current_x - self.prev_x
            delta_y = current_y - self.prev_y
            delta_time = (current_time - self.prev_time).to_sec()

            distance = math.sqrt(delta_x**2 + delta_y**2)
            speed = distance / delta_time
            speed_kmh = speed * 3.6

            speed_msg = Float64()
            speed_msg.data = speed_kmh
            self.speed_pub.publish(speed_msg)


        self.prev_x = current_x
        self.prev_y = current_y
        self.prev_time = current_time

if __name__ == '__main__':
    try:
        UTMToSpeed()
    except rospy.ROSInterruptException:
        pass
