# 근사 컨투어
# 노이즈와 침식 등으로 실제 영상에서는 정확한 컨투어가 비 효율적인 경우가 많다.
# 부정확하게 단순화한 컨투어가 오히려 더 쓸모 있는 경우가 많다.

# 상처있는 사각형에 대한 컨투어 비교

import cv2
import numpy as np

img = cv2.imread("./img/bad_rect.png")
img2 = img.copy()

cv2.imshow("original", img)     # 원본 이미지

imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, th = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY)

# 컨투어 찾기
contours, hierachy = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

contour = contours[0]

# 오차 범위 지정 (전체 둘레의 0.05로)
epsilon = 0.05 * cv2.arcLength(contour, True)

# 근사 값으로 컨투어 계산 하는 함수
# cv2.approxPolyDP(대상 컨투어 좌표, 근사 값 정확도, 컨투어 닫힘 여부)
approx = cv2.approxPolyDP(contour, epsilon, True)

# 각각 컨투어 선 그리기
cv2.drawContours(img, [contour], -1, (0,255,0), 3)
cv2.drawContours(img2, [approx], -1, (0,255,0), 3)

cv2.imshow("contour", img)      # 원래의 컨투어
cv2.imshow("approx", img2)      # 들쭉날쭉한 상처를 무시한 사각형을 찾는 컨투어
cv2.waitKey()
cv2.destroyAllWindows()