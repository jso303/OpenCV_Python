# 팽창연산
# 영상 속 사물의 주변을 덧붙여 영역을 확장
# 해당 예시는 사각형 3x3 픽셀 영역 기준으로 모자란 부분에 팽창하여
# 하얀색 글자 내의 작은 점들이 덮어짐, 전체적으로 굵어짐

import cv2
import numpy as np

img = cv2.imread("./img/morph_hole.png")

k = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))

# cv2.dilate(입력영상, 구조화 요소 커널 객체)
dst = cv2.dilate(img, k)

merged = np.hstack((img, dst))
cv2.imshow("Dilation", merged)
cv2.waitKey(0)
cv2.destroyAllWindows()