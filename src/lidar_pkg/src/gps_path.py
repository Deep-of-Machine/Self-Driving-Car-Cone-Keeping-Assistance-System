#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import NavSatFix
import atexit

# 리스트 초기화
path_x = []
path_y = []

# Callback 함수 정의
def callback(data):
    global path_x, path_y
    path_x.append(data.latitude)
    path_y.append(data.longitude)

# 프로그램 종료 시 실행할 함수
def on_exit():
    global path_x, path_y
    print("path_x:", path_x)
    print("path_y:", path_y)

# 노드 초기화
rospy.init_node('coordinate_listener', anonymous=True)

# Subscriber 생성
rospy.Subscriber('/ublox_gps/fix', NavSatFix, callback)

# 프로그램 종료 시 on_exit 함수 실행
atexit.register(on_exit)

# Spin
rospy.spin()
