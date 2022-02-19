# 열림과 닫힘 연산으로 노이즈 제거

# 침식과 팽창 연산을 조합하는 방식
# 열림 연산 : 침식 후 팽창      밝은 노이즈 제거, 객체 분리, 돌출된 픽셀 제거
# 닫힘 연산 : 팽창 후 침식      어두운 노이즈 제거, 끊어지는 객체 연결, 구멍 매우기

# 원래 크기를 유지한 채 노이즈 제거

import cv2
import numpy as np

img1 = cv2.imread("./img/morph_dot.png", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("./img/morph_hole.png", cv2.IMREAD_GRAYSCALE)

k = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))

# cv2.morphologyEx(입력 영상, 모폴로지 연산 종류 지정, 구조화 요소 커널)
opening = cv2.morphologyEx(img1, cv2.MORPH_OPEN, k)
closing = cv2.morphologyEx(img2, cv2.MORPH_CLOSE, k)

merged1 = np.hstack((img1, opening))
merged2 = np.hstack((img2, closing))
merged3 = np.vstack((merged1, merged2))
cv2.imshow("opening, closing", merged3)
cv2.waitKey(0)
cv2.destroyAllWindows()