import cv2
import numpy as np

win_name = "Trackbar"

img = cv2.imread("./img/Ch02_img/blank_500.jpg")
cv2.imshow(win_name, img)

# 트랙바 이벤트 처리함수
def onChange(x):
    print(x)
    r = cv2.getTrackbarPos("R", win_name)
    g = cv2.getTrackbarPos("G", win_name)
    b = cv2.getTrackbarPos("B", win_name)
    print(r,g,b)
    img[:] = [b,g,r]    # 기존 이미지에 픽셀 값 적용
    cv2.imshow(win_name, img)
    
# cv2.createTrackbar("트랙바 이름", 트랙바 창 이름, 초기 값, 눈금 개수, 트랙바 핸들러 함수)    
cv2.createTrackbar("R", win_name, 255, 255, onChange)
cv2.createTrackbar("G", win_name, 255, 255, onChange)
cv2.createTrackbar("B", win_name, 255, 255, onChange)

while True:
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()