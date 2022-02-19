# 침식 연산
# 기존에 있던 객체의 영역을 깍아내는 연산
# 해당 예시는 사각형 3x3 픽셀 영역 기준으로 깍아내어 작은 점들 제거, 전체적으로 얇아짐

import cv2
import numpy as np

img = cv2.imread("./img/morph_dot.png")

# cv2.getStructuringElement(구조화 요소 커널의 모양, 커널크기)
# 모양 종류 : 사각형 cv2.MORPH_RECT, 타원형 cv2.MORPH_ELLIPSE, 십자형 cv2.MORPH_CROSS
k = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))

# cv2.erode(입력영상, 구조화 요소 커널 객체)
erosion = cv2.erode(img, k)

merged = np.hstack((img, erosion))
cv2.imshow("Erode", merged)
cv2.waitKey(0)
cv2.destroyAllWindows()