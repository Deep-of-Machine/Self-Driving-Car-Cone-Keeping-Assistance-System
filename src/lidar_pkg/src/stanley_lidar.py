#!/usr/bin/env python3

import numpy as np
import rospy
from sensor_msgs.msg import PointCloud2
import sensor_msgs.point_cloud2 as pc2
from std_msgs.msg import Float64

class StanleyController:
    def __init__(self):
        self.midpoints = None
        self.lookahead_distance = 2.0  # 임의의 값
        self.max_steering_angle = np.radians(20)  # 최대 조향각 

        self.sub = rospy.Subscriber('/path_planning', PointCloud2, self.path_callback)
        self.pub = rospy.Publisher('/steering_angle', Float64, queue_size=10)
        
    def path_callback(self, msg):
        self.midpoints = np.array(list(pc2.read_points(msg, skip_nans=True, field_names=("x", "y", "z"))))
        self.control()

    def control(self):
        if self.midpoints is None:
            return

        # Vehicle position (assuming it's at (0,0) for simplicity)
        vehicle_pos = np.array([0, 0])

        # Find the point in the path that's closest to the vehicle within the lookahead distance
        distances = np.linalg.norm(self.midpoints[:, :2] - vehicle_pos, axis=1)
        idx = np.argmin(distances)
        lookahead_point = self.midpoints[idx]

        # Calculate the heading error
        path_heading = np.arctan2(lookahead_point[1], lookahead_point[0])
        heading_error = path_heading

        # Calculate steering angle using Stanley controller
        steering_angle = np.arctan2(self.lookahead_distance * np.sin(heading_error), 1)
        
        # Clamp the steering angle to the maximum value
        steering_angle = np.clip(steering_angle, -self.max_steering_angle, self.max_steering_angle)

        self.pub.publish(steering_angle)
        print(f"Steering Angle: {np.degrees(steering_angle)} degrees")

if __name__ == '__main__':
    rospy.init_node('stanley_controller')
    controller = StanleyController()
    rospy.spin()