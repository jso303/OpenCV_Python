# 컬러 이미지 그레이 스케일로 변환하는 방법

import cv2
import numpy as np

img = cv2.imread("./img/girl.jpg")
img2 = img.astype(np.uint16)            # dtype 변경(1)
b,g,r = cv2.split(img2)                 # 채널별로 분리(2)
gray1 = ((b+g+r)/3).astype(np.uint8)    # brg 평균 값 연산 후 dtype 변경(3)

gray2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   # OpenCV에서 제공하는 함수 (1,2,3 과정 자동 진행)

cv2.imshow("original", img)
cv2.imshow("gray1", gray1)
cv2.imshow("gray2", gray2)

cv2.waitKey(0)
cv2.destroyAllWindows()