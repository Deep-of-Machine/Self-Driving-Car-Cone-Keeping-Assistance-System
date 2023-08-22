import cv2
import numpy as np

# 사용자 설정 파라미터
VIDEO_PATH = "/home/baqu/Self-Driving-Car-Cone-Keeping-Assistance-System/src/22_LKAS/baqu4_main/scripts/source/output_15_line.mp4"
IMAGE_H = 480
IMAGE_W = 640
ROI_Y_START = 140  # ROI 시작 Y 좌표
ROI_HEIGHT = IMAGE_H  # ROI 높이
TARGET_X1 = 300  # 원근 변환 목표 x 좌표 1
TARGET_X2 = 340  # 원근 변환 목표 x 좌표 2 (조금 더 큰 값)
import time

# 원근 변환을 위한 설정
src = np.float32([[0, IMAGE_H], [IMAGE_W, IMAGE_H], [0, 0], [IMAGE_W, 0]])
dst = np.float32([[TARGET_X1, IMAGE_H], [TARGET_X2, IMAGE_H], [0, 0], [IMAGE_W, 0]])
M = cv2.getPerspectiveTransform(src, dst)  # 변환 행렬

# VideoCapture 객체 생성
cap = cv2.VideoCapture(VIDEO_PATH)

# 영상 파일이 정상적으로 열렸는지 확인
if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

while True:
    # 프레임 읽기
    ret, frame = cap.read()

    # 영상을 다 읽으면 종료
    if not ret:
        break

    # 프레임 리사이즈
    frame_resized = cv2.resize(frame, (IMAGE_W, IMAGE_H))

    # 프레임 처리 (원하는 작업 수행)
    img = frame_resized[ROI_Y_START:(ROI_Y_START + ROI_HEIGHT), 0:IMAGE_W]  # ROI 설정
    warped_img = cv2.warpPerspective(img, M, (IMAGE_W, IMAGE_H))  # 이미지 원근 변환

    # 결과 영상 출력
    cv2.imshow("Resized Frame", frame_resized)
    cv2.imshow("Warped Frame", warped_img)
    time.sleep(0.1)

    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 리소스 해제
cap.release()
cv2.destroyAllWindows()
