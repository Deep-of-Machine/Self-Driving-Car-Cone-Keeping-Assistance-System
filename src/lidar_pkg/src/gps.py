#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import NavSatFix

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
