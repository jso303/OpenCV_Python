# 허프 원 검출
# cv2.HoughCircles 함수를 이용해 허프 원 검출
# 캐니 엣지 수행 수 소벨 필터로 엣지의 경사도를 누적하여 검출하는 방식

import cv2
import numpy as np

img = cv2.imread("./img/coins_spread1.jpg")
img2 = img.copy()
gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# 노이즈 제거(가우시안 블러)
blur = cv2.GaussianBlur(gray, (3,3), 0)

# cv2.HoughCircles(입력 영상, 검출 방식 선택, 입력 영상과 경사 누적의 해상도 반비례율(1:입력값과 동일, 클 수록 부정확),\
# 원들 중심 간 최소 거리(0은 불가), 검출 원 결과, 캐니 엣지에 전달할 스레시홀드 최대 값(최소 값은 최대 값의 1/2)
circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1.5, 100, None, 300)
if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        cv2.circle(img2, (i[0], i[1]),i[2], (0,255,0), 2)
        cv2.circle(img2, (i[0], i[1]), 2, (0,0,255), 5)
        
merged = np.hstack((img, img2))
cv2.imshow("hough circle", merged)
cv2.waitKey()
cv2.destroyAllWindows()