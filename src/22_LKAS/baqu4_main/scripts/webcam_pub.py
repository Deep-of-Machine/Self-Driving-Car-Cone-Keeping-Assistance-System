#!/usr/bin/env python

import rospy
import cv2

from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

cap = cv2.VideoCapture(2)
#"/home/hwb/Desktop/uuuu/video/wave.mp4"
#"/home/jobalchi/baqu4_final/src/baqu4_run/scripts/source/WIN_20220925_14_36_35_Pro.mp4"
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360) 
cap.set(cv2.CAP_PROP_FPS, 30)

rospy.init_node("webcam_pub", anonymous=True)
image_pub = rospy.Publisher("webcam_image", Image, queue_size=1)

bridge = CvBridge()

while not rospy.is_shutdown():
    # Capture frame-by-frame
    ret, cv_image = cap.read()
    #cv_image = cv2.resize(cv_image, dsize=(640, 360), interpolation=cv2.INTER_AREA)

    if cv2.waitKey(1) == 27:
        break  # esc to quit

    # Display the resulting frame
    image_pub.publish(bridge.cv2_to_imgmsg(cv_image, "bgr8"))
    #cv2.imshow('Image pub',cv_image)
    cv2.waitKey(10)
    


# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
