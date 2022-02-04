import cv2
import numpy as np
import matplotlib.pylab as plt

img = cv2.imread("./img/girl.jpg")

mask = np.zeros_like(img)                               # img와 같은 크기의 0(검은색)으로 가득 찬 이미지 생성
cv2.circle(mask, (150,140), 100, (255,255,255), -1)     # 150,140 위치에 반지름 100인 255(흰색) 원 그리기 

masked = cv2.bitwise_and(img, mask) # 원 이외의 부분을 0(검은색)으로 처리

# 위 세 줄을 아래 방식으로 2차원 배열 만으로도 연산 가능
# mask = np.zeros(img,shape[:2], dtype=np.uint8)
# cv2.circle(mask, (150,140), 100, (255), -1)
# masked = cv2.bitwise_and(img,img,mask=mask)

cv2.imshow("original", img)
cv2.imshow("mask", mask)
cv2.imshow("masked", masked)
cv2.waitKey()
cv2.destroyAllWindows()