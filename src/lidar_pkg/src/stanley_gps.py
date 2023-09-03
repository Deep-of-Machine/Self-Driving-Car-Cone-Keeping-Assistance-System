import rospy
import math
import numpy as np
from sensor_msgs.msg import Imu, NavSatFix
from std_msgs.msg import Float64
from pyproj import Proj

class StanleyControlNode:
    def __init__(self):
        self.imu_yaw = 0.0
        self.gps_lat = None
        self.gps_lon = None
        self.v = 5.0  # 초기 속도
        self.max_steering_angle = 0.52  # 라디안, 최대 조향각
        self.k = 0.5  # Stanley controller tuning parameter
        self.path_x = []  # Placeholder for path's x-coordinates
        self.path_y = []  # Placeholder for path's y-coordinates

        # UTM 변환을 위한 객체 (Zone 52로 변경)
        self.utm_converter = Proj(proj="utm", zone=52, ellps="WGS84")

        rospy.init_node('stanley_control_node', anonymous=True)
        rospy.Subscriber("/filtered/imu/yaw", Imu, self.imu_callback)
        rospy.Subscriber("/ublox_gps/fix", NavSatFix, self.gps_callback)
        rospy.Subscriber("/gps_speed", Float64, self.gps_speed_callback)
        self.pub = rospy.Publisher("/steering_angle", Float64, queue_size=10)

    def imu_callback(self, data):
        self.imu_yaw = data.data

    def gps_speed_callback(self, data):
        self.v = 5 # data.data

    def gps_callback(self, data):
        self.gps_lat = data.latitude
        self.gps_lon = data.longitude

    def get_cartesian_coords(self, lat, lon):
        x, y = self.utm_converter(lon, lat)
        return x, y

    def stanley_control(self, x, y, yaw, v, cx, cy):
        dx = [x - icx for icx in cx]
        dy = [y - icy for icy in cy]
        d = np.hypot(dx, dy)

        # 차량 헤딩을 고려하여 앞에 있는 점만 고려
        angles = [math.atan2(dy[i], dx[i]) for i in range(len(dx))]
        angles = np.array(angles) - yaw
        angles = np.abs(((angles + np.pi) % (2 * np.pi)) - np.pi)  # Normalize angles to -pi to pi
        forward_indices = np.where(angles <= np.pi / 2)[0]
        
        if len(forward_indices) == 0:
            target_idx = len(cx) - 1  # Fallback: use the last point if no point is ahead.
        else:
            d_forward = d[forward_indices]
            lookahead_distance = np.abs(v)
            target_idx = forward_indices[np.argmin(np.abs(d_forward - lookahead_distance))]

        target_theta = math.atan2(cy[target_idx] - y, cx[target_idx] - x)
        theta_e = target_theta - yaw

        delta = theta_e + math.atan2(self.k * d[target_idx], v)
        return delta, target_idx

    def run(self):
        rate = rospy.Rate(10)
        while not rospy.is_shutdown():
            if self.gps_lat is not None and self.gps_lon is not None:
                x, y = self.get_cartesian_coords(self.gps_lat, self.gps_lon)
                delta, _ = self.stanley_control(x, y, self.imu_yaw, self.v, self.path_x, self.path_y)
                
                delta = max(min(delta, self.max_steering_angle), -self.max_steering_angle)
                
                self.pub.publish(delta)
            rate.sleep()

if __name__ == '__main__':
    try:
        node = StanleyControlNode()
        node.run()
    except rospy.ROSInterruptException:
        pass
