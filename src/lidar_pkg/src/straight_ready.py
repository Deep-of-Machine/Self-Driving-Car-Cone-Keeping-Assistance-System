#!/usr/bin/env python3

import numpy as np
import rospy
from std_msgs.msg import Float64
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# UTM 경로 (이미 변환된 UTM x, y 좌표)
path_x = [308367.62720373285, 308367.4881663536, 308367.3339387842, 308367.18428057805, 308366.8211367342, 308366.45926223695, 308366.0864926249, 308365.68687616393, 308365.3412074746, 308364.93551922846, 308364.5204590069, 308364.08690859925, 308363.64017834165, 308363.2691862757, 308362.9437853347, 308362.54746968375, 308362.1417820514, 308361.62161958544, 308361.1285580025, 308360.6785489452, 308360.2715923942, 308359.96036666026, 308359.6460946158, 308359.40779373026, 308359.37436727795]
path_y = [4130212.460293282, 4130212.5855940725, 4130212.822260487, 4130213.2586549623, 4130214.055191487, 4130214.9072080455, 4130215.6706593977, 4130216.423623166, 4130217.2086581667, 4130218.0838808124, 4130218.9371142755, 4130219.7574653565, 4130220.3893872113, 4130221.230510738, 4130222.1261002887, 4130223.02331228, 4130223.89853509, 4130224.809682387, 4130225.7424133136, 4130226.6186502324, 4130227.438393135, 4130228.1782331727, 4130228.784921184, 4130229.2233438976, 4130229.312923149]

# 실시간으로 업데이트될 IMU Yaw 값
current_yaw = 0.0

# ROS 콜백 함수: Yaw 값을 업데이트
def imu_callback(data):
    global current_yaw
    current_yaw = data.data

# ROS 노드 초기화
rospy.init_node('imu_plotter', anonymous=True)

# ROS 토픽 구독
rospy.Subscriber("/filtered/imu/yaw", Float64, imu_callback)

# 그래프 설정
fig, ax = plt.subplots()
sc = ax.scatter(path_x, path_y, label='Path', color='b')

# 실시간 그래프 업데이트 함수
def update(frame):
    global current_yaw
    ax.clear()

    # 경로 표시
    ax.scatter(path_x, path_y, label='Path', color='b')

    # 현재 위치와 방향 (Yaw) 표시 (임의로 현재 위치를 설정함)
    current_x, current_y = path_x[-1], path_y[-1]  # 마지막 경로 포인트를 현재 위치로 가정

    # Yaw 값이 -pi에서 +pi 사이라고 가정
    # Yaw 방향을 화살표로 표시
    arrow_length = 10.0
    arrow_dx = arrow_length * np.cos(current_yaw)  # Yaw 값은 이미 라디안 단위
    arrow_dy = arrow_length * np.sin(current_yaw)  # Yaw 값은 이미 라디안 단위
    ax.arrow(current_x, current_y, arrow_dx, arrow_dy, head_width=1, head_length=1, fc='k', ec='k')

    ax.legend()
    ax.relim()
    ax.autoscale_view()

# 애니메이션
ani = animation.FuncAnimation(fig, update, frames=range(0, 100), blit=False, cache_frame_data=False)

plt.show()