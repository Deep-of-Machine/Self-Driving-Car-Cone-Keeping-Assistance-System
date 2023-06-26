import rospy
from sensor_msgs.msg import PointCloud2, PointField
import numpy as np
import sensor_msgs.point_cloud2 as pc2

def pointcloud_callback(msg):
    pc_data = pc2.read_points(msg, skip_nans=True, field_names=("x", "y", "z", "intensity"))
    pc_array = np.array(list(pc_data))
    
    # Filter points based on distance threshold
    filtered_pc_array = []
    for point in pc_array:
        x, y, z, intensity = point
        distance = np.sqrt(x**2 + y**2 + z**2)  # Calculate Euclidean distance
        if distance < distance_threshold:  # Set your desired distance threshold
            filtered_pc_array.append(point)
    
    filtered_pc_array = np.array(filtered_pc_array)
    
    # Convert numpy array back to PointCloud2
    header = msg.header
    pc2_msg = pc2.create_cloud_xyz32(header, filtered_pc_array[:, :3])
    
    # Publish the filtered point cloud
    pub.publish(pc2_msg)
    
    rospy.loginfo("Callback: Point cloud data processed and published!")

def listener():
    rospy.init_node('pointcloud_listener', anonymous=True)
    rospy.Subscriber('/os_cloud_node/points', PointCloud2, pointcloud_callback)
    rospy.spin()

if __name__ == '__main__':
    pub = rospy.Publisher('/filtered_point_cloud', PointCloud2, queue_size=10)
    distance_threshold = 3.5  # Set your desired distance threshold
    listener()
