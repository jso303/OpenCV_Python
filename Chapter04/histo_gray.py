# 그레이 스케일 1채널 히스토그램
# 히스토그램이란 전체 영상에서 픽셀들의 색상이나 명암의 분포를 파악하는 밥법

import cv2
import numpy as np
import matplotlib.pylab as plt

# 이미지를 그레이 스케일로 읽고 출력
img = cv2.imread("./img/mountain.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("img", img)

# 히스토그램 계산 및 그리기
# calcHist(입력 영상, 처리할 채널, 마스크 지정, 픽셀 값 범위 갯수, 픽셀 값의 범위)
# 처리할 채널 : 1채널 = [0], 2채널 = [1], 3채널 = [2]
# RGB인 경우 픽셀 값의 범위 = [0, 256]
hist = cv2.calcHist([img], [0], None, [256], [0,256])
plt.plot(hist)

# 히스토그램의 배열 shape = (256, 1)
print(hist.shape)
# 히스토그램의 합, 이미지 배열 shape = 270000, (450, 600)
print(hist.sum(), img.shape)
plt.show()
