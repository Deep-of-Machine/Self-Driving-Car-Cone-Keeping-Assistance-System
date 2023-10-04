#!/usr/bin/env python3

import can
import rospy
from std_msgs.msg import Int16
import time
import os
import subprocess
from multiprocessing import Process

class RosToCan:
    def __init__(self):
        self.can0 = can.interface.Bus(channel='can0', bustype='socketcan')
        self.asms_data = 3
        self.brake_data = 0
        self.motor_data = 0
        self.steering_data = 0
        self.steering_self_data = 0
        self.voltage_brake_data = 0
            
        rospy.Subscriber('/ASMS', Int16, self.asms_callback)
        rospy.Subscriber('/brake', Int16, self.brake_callback)
        rospy.Subscriber('/motor', Int16, self.motor_callback)
        rospy.Subscriber('/steering_angle', Int16, self.steering_callback)
        rospy.Subscriber('/voltage_brake', Int16, self.voltage_brake_callback)
        rospy.Subscriber('/steering_angle_self',Int16, self.steering_self_callback)

    def steering_self_callback(self,msg):
        self.steering_self_data=msg.data
        print('steering_self_callback')

    def steering_callback(self, msg):
        self.steering_data = msg.data
        print('steering_callback')
        self.send_combined_can_message()

    def brake_callback(self, msg):
        self.brake_data = msg.data
        print('brake_callback')
        self.send_combined_can_message()

    def motor_callback(self, msg):
        self.motor_data = msg.data
        print('motor_callback')
        self.send_combined_can_message()
    
    def voltage_brake_callback(self, msg):
        self.voltage_brake_data = msg.data
        print('voltage_brake callback')
        self.send_Combined_Can_message()

    def asms_callback(self, msg):
        self.asms_data = msg.data
        print('asms_callback')
        self.send_combined_can_message()

    def send_combined_can_message(self):
        #time.sleep(0.2)
        if self.asms_data == 3:
            combined_data = [self.asms_data, 0, 0, self.steering_self_data, 0, 0, 0, 0]
        elif self.asms_data == 2:
            combined_data = [self.asms_data, 0, 0, self.steering_data, 1, 0, 0, 0]
        elif self.asms_data == 1:
            combined_data = [self.asms_data, self.motor_data, self.voltage_brake_data, self.steering_data, self.brake_data, 0, 0, 0]
        msg = can.Message(is_extended_id=False, arbitration_id=0x123, data=combined_data)
        
        try:
            self.can0.send(msg)
            print("Sent Combined CAN message: ID={}, Data={}".format(msg.arbitration_id, msg.data))
            # rospy.sleep(1)
        except can.CanError:
            print("Failed to send CAN message")

if __name__ == '__main__':
    os.system('sudo ifconfig can0 down')
    os.system('sudo ifconfig can1 down')

    os.system('sudo ip link set can0 type can bitrate 500000')
    os.system('sudo ifconfig can0 up')
    os.system('sudo ip link set can1 type can bitrate 500000')
    os.system('sudo ifconfig can1 up')

    steering_process = Process(target=subprocess.run, args=(['./steering_both'],))
    motor_process = Process(target=subprocess.run, args=(['./motor'],))
    brake_process = Process(target=subprocess.run, args=(['./brake'],))
    
    motor_process.start()
    steering_process.start()
    brake_process.start()
    
    rospy.init_node('ros_to_combined_can_node')
    ros_to_can = RosToCan()
    rospy.spin()
