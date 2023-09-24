import rospy
from sensor_msgs.msg import PointCloud2, PointField
import numpy as np
import sensor_msgs.point_cloud2 as pc2
from sklearn.cluster import DBSCAN

def cluster_objects(pc_array):
    clustering = DBSCAN(eps=0.4, min_samples=2)  
    labels = clustering.fit_predict(pc_array[:, :3])  

    unique_labels = np.unique(labels) 
    object_centroids = [] 

    for label in unique_labels:
        if label == -1: 
            continue

        cluster_points = pc_array[labels == label]  
        centroid = np.mean(cluster_points[:, :3], axis=0) 
        object_centroids.append(centroid) 

    return object_centroids

def pointcloud_callback(msg):
    pc_data = pc2.read_points(msg, skip_nans=True, field_names=("x", "y", "z"))
    pc_array = np.array(list(pc_data))  


    filtered_pc_array = []
    for point in pc_array:
        x, y, z = point
        distance = np.sqrt(x**2 + y**2 + z**2)  
        if (distance < distance_threshold) and x > 0.5:  #and (abs(x) > 1 or abs(y) > 2) and x > 1: #x > -1.6:  #(abs(x) > 1 or abs(y) > 2)
            filtered_pc_array.append(point)
   
    filtered_pc_array = np.array(filtered_pc_array)

    object_centroids = cluster_objects(filtered_pc_array)  
    # print(object_centroids)

    header = msg.header
    fields = [
        PointField(name="x", offset=0, datatype=PointField.FLOAT32, count=1),
        PointField(name="y", offset=4, datatype=PointField.FLOAT32, count=1),
        PointField(name="z", offset=8, datatype=PointField.FLOAT32, count=1)
    ]
    pc2_msg = pc2.create_cloud(header, fields, object_centroids)  

    pub.publish(pc2_msg)  

    rospy.loginfo("Callback: Point cloud data processed and published!")

def listener():
    rospy.init_node('pointcloud_listener', anonymous=True)  
    rospy.Subscriber('/filtered_point_cloud', PointCloud2, pointcloud_callback) 
    rospy.spin() 

if __name__ == '__main__':
    pub = rospy.Publisher('/object_centroids', PointCloud2, queue_size=10) 
    distance_threshold =  20 #속도가 빨라지면 distance_threshold 증가,느려지면 감소.
    listener() 
