#!/usr/bin/env python3

import pygame
import os
from std_msgs.msg import Int16
import rospy

MUSIC_PATH = "/home/baqu/Self-Driving-Car-Cone-Keeping-Assistance-System/src/main_pkg/music/robotcar.mp3"

# 이전에 받은 데이터 값을 저장할 변수
prev_data = None

def asms_callback(data):
    global prev_data  # 전역 변수 사용

    if prev_data != data.data:  # 이전 데이터와 현재 데이터가 다를 경우만 실행
        if data.data == 1:
            pygame.mixer.init()
            pygame.mixer.music.load(MUSIC_PATH)
            pygame.mixer.music.play()
        else:
            pygame.mixer.init()
            pygame.mixer.music.stop()

        prev_data = data.data  # 현재 데이터를 이전 데이터로 저장

def asms_subscriber():
    rospy.init_node('asms_subscriber', anonymous=True)
    rospy.Subscriber("/ASMS", Int16, asms_callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        asms_subscriber()
    except rospy.ROSInterruptException:
        pass
