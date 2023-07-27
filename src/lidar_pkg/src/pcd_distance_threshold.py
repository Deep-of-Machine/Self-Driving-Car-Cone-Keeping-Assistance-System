import rospy
import sensor_msgs.point_cloud2 as pc2
from sensor_msgs.msg import PointCloud2
import numpy as np

def filter_pointcloud(data):
    pc_data = pc2.read_points(data, skip_nans=True, field_names=("x", "y", "z"))
    pc_array = np.array(list(pc_data))
    
    # Define distance threshold
    distance_threshold = 20.0  # meters
    
    # Calculate the distance from (0,0,0)
    distances = np.sqrt(np.sum(np.square(pc_array), axis=1))
    
    # Filter points based on the distance
    filtered_indices = distances < distance_threshold
    filtered_pc_array = pc_array[filtered_indices]
    
    # Convert back to pointcloud2 and publish
    header = data.header
    filtered_pc2_msg = pc2.create_cloud_xyz32(header, filtered_pc_array.tolist())
    pub.publish(filtered_pc2_msg)

def listener():
    rospy.init_node('pointcloud_listener', anonymous=True)
    rospy.Subscriber('/os_cloud_node/points', PointCloud2, filter_pointcloud)
    rospy.spin()

if __name__ == '__main__':
    # Define the publisher globally
    pub = rospy.Publisher('/filtered_point_cloud', PointCloud2, queue_size=10)

    listener()
