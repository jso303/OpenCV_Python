# 바이레터널 필터와 가우시안 필터 비교하기
# 블러링 필터의 잡음 제거시 경계의 흐릿함 문제를 해결함
# 대신 바이레터널 필드는 영상 처리가 느림

import cv2
import numpy as np

img = cv2.imread("./img/gaussian_noise.jpg")

blur1 = cv2.GaussianBlur(img, (5,5), 0)

# cv2.bilateralFilter(입력영상, 필터 직경, 색공간 필터의 시그마 값, 좌표 공간의 시그마 값)
blur2 = cv2.bilateralFilter(img, 5, 75, 75)

merged = np.hstack((img, blur1, blur2))
cv2.imshow("bilateral", merged)
cv2.waitKey(0)
cv2.destroyAllWindows()