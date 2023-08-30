#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import NavSatFix

from pyproj import Proj

# UTM 좌표계 정의 (Zone 52, WGS84)
utm_proj = Proj(proj='utm', zone=52, ellps='WGS84')

# 위경도 좌표 (예: 서울)
latitude = 37.5665
longitude = 126.9780

# 위경도를 UTM (x, y) 좌표로 변환
x, y = utm_proj(longitude, latitude)

print(f"UTM x: {x}, UTM y: {y}")


def gps_callback(msg):
    # GPS 데이터를 처리하거나 변환하는 코드가 필요한 경우 여기에 추가합니다.
    # 현재는 받은 GPS 데이터를 그대로 발행합니다.
    pub.publish(msg)

def listener():
    rospy.init_node('gps_listener', anonymous=True)
    
    # GPS 데이터를 받기 위한 Subscriber 설정
    rospy.Subscriber('/gps_input', NavSatFix, gps_callback)
    
    rospy.spin()

if __name__ == '__main__':
    # GPS 데이터를 발행하기 위한 Publisher 설정
    pub = rospy.Publisher('/gps_output', NavSatFix, queue_size=10)
    
    listener()
