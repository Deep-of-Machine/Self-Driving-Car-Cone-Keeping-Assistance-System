#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

def asmscallback(data):
    servo_pub = rospy.Publisher('servo_asms', Int32, queue_size=1)
    linear_pub = rospy.Publisher('linear_asms', Int32, queue_size=1)
    motor_pub = rospy.Publisher('motor_asms', Int32, queue_size=1)
    
    servo_pub.publish(data.data)
    linear_pub.publish(data.data)
    motor_pub.publish(data.data)
    
def asms():
    rospy.init_node('asms_relay', anonymous=True)

    rospy.Subscriber("asms_control", Int32, asmscallback)

    rospy.spin()

if __name__ == '__main__':
    asms()