#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Imu
from std_msgs.msg import Float64, Header
import math
import tf

def quaternion_to_yaw(quaternion):
    # Convert quaternion to Euler angles
    euler = tf.transformations.euler_from_quaternion([quaternion.x, quaternion.y, quaternion.z, quaternion.w])
    # Extract yaw value
    yaw = euler[2]
    return yaw

def imu_callback(imu_msg):
    # 필터링할 데이터를 추출합니다.
    filtered_data = Imu()
    filtered_data.header = Header()
    filtered_data.header.stamp = rospy.Time.now()
    filtered_data.header.frame_id = imu_msg.header.frame_id
    filtered_data.orientation = imu_msg.orientation
    filtered_data.angular_velocity = imu_msg.angular_velocity
    filtered_data.linear_acceleration = imu_msg.linear_acceleration

    # yaw 값을 계산합니다.
    yaw_value = quaternion_to_yaw(imu_msg.orientation)
    
    # 새로운 토픽으로 데이터를 publish합니다.

    yaw_pub.publish(yaw_value)

if __name__ == '__main__':
    rospy.init_node('imu_data_filter')

    # 원본 /imu/data 토픽을 구독합니다.
    imu_sub = rospy.Subscriber('/imu/data', Imu, imu_callback)

    yaw_pub = rospy.Publisher('/filtered/imu/yaw', Float64, queue_size=10)

    rospy.spin()
