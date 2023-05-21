#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import cv2
import math
import time

from std_msgs.msg import Float32
from std_msgs.msg import Int32
from sensor_msgs.msg import Image
import rospy

from preprocessing import *
from stopDetector import *

cap = cv2.VideoCapture(0)
#"/home/hwb/Desktop/uuuu/video/wave.mp4"
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360) 
cap.set(cv2.CAP_PROP_FPS, 30)

rospy.init_node('detect_steering', anonymous=True)
pub = rospy.Publisher('servo_angle', Float32, queue_size=1)
pub2 = rospy.Publisher('stop_sign', Int32, queue_size=1)
rate = rospy.Rate(30) # 10hz

path = "./source/WIN_20220925_14_36_35_Pro.mp4"
obj_b = cv2.imread('/home/jobalchi/baqu4_final/src/baqu4_run/scripts/source/corn_data/lavacorn_nb.png', cv2.IMREAD_GRAYSCALE)#wad
obj_s = cv2.imread('/home/jobalchi/baqu4_final/src/baqu4_run/scripts/source/corn_data/lavacorn_ns.png', cv2.IMREAD_GRAYSCALE)#wad

obj_contours_b,_=cv2.findContours(obj_b, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)#wad
obj_contours_s,_=cv2.findContours(obj_s, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)#wad
obj_pts_b=obj_contours_b[0]#wad
obj_pts_s=obj_contours_s[0]#wad

WIDTH  = 640
HEIGHT = 360

kernel_size=5

low_threshold=20
high_threshold=255

theta=np.pi/180

p_r_m=0
p_r_n=0
p_l_m=0
p_l_n=0

lower_blue = (115-30, 10, 10) # hsv 이미지에서 바이너리 이미지로 생성 , 적당한 값 30
upper_blue = (115+30, 255, 255)

lower_red = (6-6, 30, 30) # hsv 이미지에서 바이너리 이미지로 생성 , 적당한 값 30
upper_red = (6+4, 255, 255)

lower_yellow = (19-4, 30, 30) # hsv 이미지에서 바이너리 이미지로 생성 , 적당한 값 30
upper_yellow = (19+30, 255, 255)

isUseableRed=False
isInStopArea=False

def main():
    global p_r_m
    global p_r_n
    global p_l_m
    global p_l_n
    global isUseableRed
    global isInStopArea
    print(3)
    global img
    ret, img = cap.read()
    cv2.imshow("Image sub", img)
    cv2.waitKey(1)

    t=time.time()
    img = cv2.resize(img, dsize=(int(WIDTH), int(HEIGHT)))

    img_thresh = preprocessing(img, low_threshold, high_threshold, kernel_size)

##    작업공간    ##
    contours,_=cv2.findContours(img_thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    points = []
    isSameCorn=False
    for pts in contours:
        if cv2.contourArea(pts) <100:
            continue
        rc=cv2.boundingRect(pts)
        dist_b=cv2.matchShapes(obj_pts_b, pts, cv2.CONTOURS_MATCH_I3, 0)
        dist_s=cv2.matchShapes(obj_pts_s, pts, cv2.CONTOURS_MATCH_I3, 0)
        if dist_b <0.9 or dist_s<0.7:
            mid_x = (2*rc[0]+rc[2])/2
            for p in points:
                if p[0]<=mid_x and p[2]>=mid_x:
                    isSameCorn=True
                    break
            if not isSameCorn and 40<=mid_x<=600:
                cv2.rectangle(img_thresh, rc, (255, 0,0),1)
                points.append([rc[0], rc[1], rc[0]+rc[2], rc[1]+rc[3]])
            isSameCorn=False

    if p_r_m==0 and p_l_m==0:
        p_r_m=0.3
        p_r_n=37
        p_l_m=-0.3
        p_l_n=238

    r_mid, l_mid, s_mid = depart_points(img, points)
    
    for r in r_mid:
        cv2.circle(img, r, 10, (0, 255, 255), -1, cv2.LINE_AA) #노랑
    for l in l_mid:
        cv2.circle(img, l, 10, (255, 0, 0), -1, cv2.LINE_AA) #파랑
    
    if isUseableRed==False and isRedValueable(s_mid, p_r_m, p_r_n, p_l_m, p_l_n):
        isUseableRed=True

    if isUseableRed:
        r_mid, l_mid = depart_points_linear(s_mid, p_r_m, p_r_n, p_l_m, p_l_n)
        linear_img, cross=linear_reg(img, l_mid, r_mid)
        linear_img, y_val = findStopArea(linear_img, r_mid, l_mid, cross, p_r_n, p_r_m, p_l_n, p_l_m, isInStopArea)
        cv2.line(linear_img, (0,250), (int(WIDTH), 250), (0, 0, 255), 2)
        if 250-y_val<=0:
            isInStopArea=True
        if isInStopArea:
            print("-----정지구역 안입니다------")
            pub2.publish(1)

    else:
        linear_img, cross=linear_reg(img, l_mid, r_mid)

    dt=time.time()-t
    print("delay : ", dt)
    cv2.imshow("ex", linear_img)#lines_edges

def depart_points(img, points):
    right_line=[]
    left_line=[]
    stop_line=[]

    for p in points:
        x1, y1, x2, y2 = p
        label = plot_one_box([x1, y1, x2, y2], img)

        x = int((x1 + x2)/2)
        y = int(y2)

        if label == 'blue':
            left_line.append([x, y])
        elif label == 'yellow':
            right_line.append([x, y])
        elif label == 'red':
            stop_line.append([x, y])
        else:
            pass

    return right_line, left_line, stop_line

def hsv_inrange(h,s,v):
    if lower_blue[0] <= h <= upper_blue[0] and lower_blue[1] <=s<= upper_blue[1] and lower_blue[2] <=v<= upper_blue[2]:
        color = (255,0,0)
        label = 'blue'
    elif lower_yellow[0] <= h <= upper_yellow[0] and lower_yellow[1] <=s<= upper_yellow[1] and lower_yellow[2] <=v<= upper_yellow[2]:
        color = (0,255,255)
        label = 'yellow'
    elif lower_red[0] <= h <= upper_red[0] and lower_red[1] <=s<= upper_red[1] and lower_red[2] <=v<= upper_red[2]:
        color = (0,0,255)
        label = 'red'
    else:
        color = (0,0,0)
        label = 'another'
        
    return label, color

def plot_one_box(x, img, line_thickness=None):  # Plots one bounding box on image img
    tl = line_thickness or round(0.002 * max(img.shape[0:2])) + 1  # line thickness
    c1, c2 = (int(x[0]), int(x[1])), (int(x[2]), int(x[3]))

    colr = np.mean(img[(c1[1]+c2[1])//2:c2[1], int(0.5 * (c1[0] + c2[0])), :],axis=0)
    
    b,g,r = colr
    
    color = [b,g,r]  # BGR 순서 ; 파란색
    pixel = np.uint8([[color]]) # 한 픽셀로 구성된 이미지로 변환

    # BGR -> HSV
    hsv = cv2.cvtColor(pixel, cv2.COLOR_BGR2HSV)
    # print(hsv, 'shape:', hsv.shape )

    # 픽셀값만 가져오기 
    hsv = hsv[0][0]

    h, s, v = hsv[0], hsv[1], hsv[2]
    b,g,r=colr/np.sum(colr)

    label, color = hsv_inrange(h,s,v)

    cv2.rectangle(img, c1, c2, color, thickness=tl)
    if label:
        tf = max(tl - 1, 1)  # font thickness
        t_size = cv2.getTextSize(label, 0, fontScale=tl / 3, thickness=tf)[0]
        c2 = c1[0] + t_size[0], c1[1] - t_size[1] - 3
        cv2.rectangle(img, c1, c2, color, -1)  # filled
        cv2.putText(img, label, (c1[0], c1[1] - 2), 0, tl / 3, [225, 255, 255], thickness=tf, lineType=cv2.LINE_AA)

    return label

def gradient(p1, p2):
    return (p2[1]-p1[1])/(p1[0]-p2[0])

def y_intercept(m, p):
    return (-1)*p[1]-m*p[0]

def point2linear_distance(m,n,p):
    return abs(m*p[0]-p[1]+n)/(m**2+1)**(1/2)

def linear_reg(img, left, right):
    left_x=[]
    left_y=[]
    right_x=[]
    right_y=[]

    global p_r_m
    global p_r_n
    global p_l_m
    global p_l_n
    
    for i in range(len(left)):
        left_x.append(left[i][0])
        left_y.append(left[i][1])

    for i in range(len(right)):
        right_x.append(right[i][0])
        right_y.append(right[i][1])

    left_calculated_weight=0
    right_calculated_weight=0
    if len(left)<2:
        left_calculated_weight=p_l_m
        left_calculated_bias=p_l_n
    else:
        mean_lx=np.mean(left_x)
        mean_ly=np.mean(left_y)
        left_calculated_weight=least_square(left_x, left_y, mean_lx, mean_ly)
        left_calculated_bias=mean_ly-left_calculated_weight*mean_lx
    target_l=left_calculated_weight*WIDTH+left_calculated_bias
    print(f"y = {left_calculated_weight} * X + {left_calculated_bias}")
    
    if len(right)<2:
        right_calculated_weight=p_r_m
        right_calculated_bias=p_r_n
    else:
        mean_rx=np.mean(right_x)
        mean_ry=np.mean(right_y)
        right_calculated_weight=least_square(right_x, right_y, mean_rx, mean_ry)
        right_calculated_bias=mean_ry-right_calculated_weight*mean_rx
    target_r=right_calculated_weight*WIDTH+right_calculated_bias
    print(f"y = {right_calculated_weight} * X + {right_calculated_bias}")
    img = cv2.line(img,(int(WIDTH/2),HEIGHT),(int(WIDTH/2),int(0)),(255,0,0),3)

    cross_x = (right_calculated_bias - left_calculated_bias) / (left_calculated_weight - right_calculated_weight)
    cross_y = left_calculated_weight*((right_calculated_bias - left_calculated_bias)/(left_calculated_weight - right_calculated_weight)) + left_calculated_bias

    if np.isnan(cross_x)!=True and np.isnan(cross_y)!=True:
        img = cv2.line(img,(0,int(left_calculated_bias)),(int(WIDTH),int(target_l)),(0,0,0),10)
        img = cv2.line(img,(int(0),int(right_calculated_bias)),(WIDTH,int(target_r)),(0,0,0),10)
        cv2.circle(img, (int(cross_x), int(cross_y)), 10, (0, 0, 255), -1, cv2.LINE_AA)

        if 80 < steering_theta(left_calculated_weight, right_calculated_weight) < 100:
            print('소실점 조향 서보모터 각도: ', steering_vanishing_point(cross_x))
            pub.publish(steering_vanishing_point(cross_x))
        else:
            print("기울기 조향 서보모터 각도: ", outer_control(steering_theta(left_calculated_weight, right_calculated_weight)))
            pub.publish(steering_theta(left_calculated_weight, right_calculated_weight))
    p_l_m=left_calculated_weight
    p_r_m=right_calculated_weight
    p_l_n=left_calculated_bias
    p_r_n=right_calculated_bias
    #print('Done.')
    return img, [cross_x, cross_y]

def least_square(val_x, val_y, mean_x, mean_y):
    return ((val_x - mean_x) * (val_y - mean_y)).sum() / ((val_x - mean_x)**2).sum()

outer = 90

# 두번째 이전꺼로 저장, 현재는 그냥 저장하고 이와 다르면 모두 다 이상치

def outer_control(x):
    global outer
    if 45 < x < 135 :
        print('######### 절대 이상치 처리 ############')
    else:
        if outer - 15 < x < outer + 15:
            outer = x
            return x
        else:
            outer = x
            print('######### 상대 이상치 처리 ############')
        
        
virtual_right_line = []
virtual_left_line = []

def steering_theta(w1, w2):
    if np.abs(w1) > np.abs(w2):  # 우회전
        if w1 * w2 < 0:  #정방향 or 약간 틀어진 방향
            w1 = -w1
            angle = np.arctan(np.abs(math.tan(w1) - math.tan(w2)) / (1 + math.tan(w1)*math.tan(w2)))
            theta = matching(angle, 0, np.pi/2, 90, 180)
        elif w1 * w2 > 0:  #극한으로 틀어진 방향
            if w1 > w2:
                theta = 90
            else:
                theta = 90
        else:
            theta = 0
    elif np.abs(w1) < np.abs(w2) :  # 좌회전
        if w1 * w2 < 0:  #정방향 or 약간 틀어진 방향
            w1 = -w1
            angle = np.arctan(np.abs(math.tan(w1) - math.tan(w2)) / (1 + math.tan(w1)*math.tan(w2)))
            theta = matching(angle, 0, np.pi/2, 90, 0)
        elif w1 * w2 > 0:  #극한으로 틀어진 방향
            if w1 > w2:
                theta = 90
            else:
                theta = 90
        else:
            theta = 0
    else:
        theta = 90

    return theta

def matching(x,input_min,input_max,output_min,output_max):
    return (x-input_min)*(output_max-output_min)/(input_max-input_min)+output_min #map()함수 정의.

def steering_vanishing_point(x):
    standard_x = int(WIDTH/2)
    diff = standard_x - x 
    if diff > 0:   #좌회전
        theta = matching(diff, 0, WIDTH/2, 90, 45)
    elif diff < 0:
        theta = matching(diff, 0, -WIDTH/2, 90, 135)

    return theta

while not rospy.is_shutdown():
    main()
    print(1)
    rospy.spin()
    print(2)

    if cv2.waitKey(10) == ord('q'):
        break
# 작업 완료 후 해제
cv2.destroyAllWindows()
