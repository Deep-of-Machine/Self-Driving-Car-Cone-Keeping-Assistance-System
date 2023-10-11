#!/usr/bin/env python3

import pygame
import os
from std_msgs.msg import Int16
import rospy

MUSIC_PATH = "/home/baqu/Self-Driving-Car-Cone-Keeping-Assistance-System/src/main_pkg/music/robotcar.mp3"

def asms_callback(data):
    if data.data == 1:
        pygame.mixer.init()
        pygame.mixer.music.load(MUSIC_PATH)
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.stop()

def asms_subscriber():
    rospy.init_node('asms_subscriber', anonymous=True)
    rospy.Subscriber("/ASMS", Int16, asms_callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        asms_subscriber()
    except rospy.ROSInterruptException:
        pass
