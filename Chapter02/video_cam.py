import cv2

cap = cv2.VideoCapture(0)               # 0번 카메라 장치 연결
if cap.isOpened():
    while True:
        ret, img = cap.read()           # 카메라 프레임 읽기
        if ret:
            cv2.imshow("camera", img)   # 프레임 이미지 표시
            if cv2.waitKey(1) != -1:    # 1ms 동안 키 입력 대기     # waitKey가 -1이 반환된다 == 키 입력이 없다.
                break                   # 아무키나 눌렀으면 중지     # waitKey가 -1 이다 == 키 입력이 들어왔다.
        else:
            print('no frame')
            break
else:
    print("can't open camera.")
cap.release()
cv2.destroyAllWindows()    