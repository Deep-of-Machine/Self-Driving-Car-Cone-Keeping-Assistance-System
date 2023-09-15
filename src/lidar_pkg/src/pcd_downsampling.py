import rospy
import sensor_msgs.point_cloud2 as pc2
from sensor_msgs.msg import PointCloud2
import numpy as np
from lidar_pkg.msg import lidar_lavacon

def remove_ground(data):
    pc_data = pc2.read_points(data, skip_nans=True, field_names=("x", "y", "z"))
    pc_array = np.array(list(pc_data))

    # Define ground threshold
    ground_threshold = -0.9  # Lidar Height
    cone_threshold = -0.3

    # Reconsidering the logic for filtering ground and other points
    non_ground_pc_array = pc_array[pc_array[:, 2] > ground_threshold]
    filtered_pc_array = non_ground_pc_array[non_ground_pc_array[:, 2] < cone_threshold]

    header = data.header 
    filtered_pc2_msg = pc2.create_cloud_xyz32(header, filtered_pc_array.tolist())
    pub.publish(filtered_pc2_msg)

def listener():
    rospy.init_node('pointcloud_listener', anonymous=True)
    rospy.Subscriber('/os_cloud_node/points', PointCloud2, remove_ground)
    rospy.spin()

if __name__ == '__main__':
    pub = rospy.Publisher('/filtered_point_cloud', PointCloud2, queue_size=10)
    listener()
