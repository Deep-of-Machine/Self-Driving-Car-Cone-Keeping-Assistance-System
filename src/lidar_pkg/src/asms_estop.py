#!/usr/bin/python

import RPi.GPIO as GPIO
from subprocess import call
import time
import rospy
from std_msgs.msg import Int32  # Integer message type from std_msgs

btnPin = 5

GPIO.setmode(GPIO.BOARD)
GPIO.setup(btnPin, GPIO.IN, GPIO.PUD_UP)

# ROS Initialization
rospy.init_node('asms_estop_publisher', anonymous=True)
pub = rospy.Publisher('asms_estop_topic', Int32, queue_size=10)

while not rospy.is_shutdown():  # Replace True with rospy.is_shutdown() for clean exit
    time.sleep(0.1)
    if GPIO.input(btnPin) == 0:
        pub.publish(3)  # Publish the number 3 to the ROS topic
