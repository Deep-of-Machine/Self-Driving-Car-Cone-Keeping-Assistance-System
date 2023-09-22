#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int16, Int8
import RPi.GPIO as GPIO
import spidev
import time

class ActuatorControl:
    def __init__(self):
        self.IN1 = 5
        self.IN2 = 6
        self.RANGE = 20

        GPIO.setwarnings(False)
        GPIO.cleanup()

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.IN1, GPIO.OUT)
        GPIO.setup(self.IN2, GPIO.OUT)

        self.spi = spidev.SpiDev()
        self.spi.open(0, 2)
        self.spi.max_speed_hz = 135000

        self.asms_status = 1
        self.initial_code_executed_for_1 = False
        self.initial_code_executed_for_3 = False
        self.previous_asms_status = None

        rospy.init_node('actuator_control_node')
        rospy.Subscriber('steering_angle', Int16, self.control_actuator)
        rospy.Subscriber('asms_status', Int8, self.asms_status_callback)

    def asms_status_callback(self, asms_status_msg):
        new_status = asms_status_msg.data
        if new_status != self.previous_asms_status:
            if new_status == 1:
                self.initial_code_executed_for_1 = False
            elif new_status == 3:
                self.initial_code_executed_for_3 = False
        self.previous_asms_status = new_status
        self.asms_status = new_status

    def analog_read(self, channel):
        r = self.spi.xfer2([1, (8 + channel) << 4, 0])
        adc_out = ((r[1] & 3) << 8) + r[2]
        return adc_out

    def control_actuator(self, steering_angle):
        sensor_data = self.analog_read(2)
        print('linear_sensor: ', sensor_data)

        if self.asms_status == 1:
            if not self.initial_code_executed_for_1:
                start_time = time.time()
                while True:
                    self.actuator_run(1)
                    end_time = time.time()
                    if (end_time - start_time) > 7:
                        break
                start_time = time.time()
                while True:
                    self.actuator_run(0)
                    end_time = time.time()
                    if (end_time - start_time) > 7:
                        break
                self.initial_code_executed_for_1 = True
            
            if steering_angle.data - self.RANGE < sensor_data < steering_angle.data + self.RANGE:
                self.actuator_stop()
            elif sensor_data < steering_angle.data - self.RANGE:
                self.actuator_run(1)
            elif sensor_data > steering_angle.data + self.RANGE:
                self.actuator_run(0)

        if self.asms_status == 3:
            if not self.initial_code_executed_for_3:
                start_time = time.time()
                while True:
                    if 556 - self.RANGE < sensor_data < 556 + self.RANGE:
                        self.actuator_stop()
                    elif 556 < steering_angle.data - self.RANGE:
                        self.actuator_run(1)
                    elif 556 > steering_angle.data + self.RANGE:
                        self.actuator_run(0)
                    end_time = time.time()
                    if (end_time - start_time) > 5:
                        break
                self.initial_code_executed_for_3 = True

    def actuator_run(self, direction):
        if direction == 0:
            GPIO.output(self.IN1, GPIO.LOW)
            GPIO.output(self.IN2, GPIO.HIGH)
        else:
            GPIO.output(self.IN1, GPIO.HIGH)
            GPIO.output(self.IN2, GPIO.LOW)

    def actuator_stop(self):
        GPIO.output(self.IN1, GPIO.HIGH)
        GPIO.output(self.IN2, GPIO.HIGH)

    def run(self):
        try:
            while not rospy.is_shutdown():
                reading = self.analog_read(2)
                voltage = reading
                time.sleep(0.3)
        except KeyboardInterrupt:
            pass
        finally:
            GPIO.cleanup()

if __name__ == "__main__":
    actuator_controller = ActuatorControl()
    actuator_controller.run()