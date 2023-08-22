import cv2

def test_webcam(webcam_index=0):
    cap = cv2.VideoCapture(webcam_index)

    if not cap.isOpened():
        print(f"Error: Cannot open webcam with index {webcam_index}")
        return

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        cv2.imshow(f'Webcam Feed - Index {webcam_index}', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# 연결된 모든 웹캠을 테스트합니다.
for i in range(4):
    test_webcam(i)
