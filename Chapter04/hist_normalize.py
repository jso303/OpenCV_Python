# 노멀라이즈(정규화) : 기준이 서로 다른 값을 같은 기준이 되게 만드는 것
# 노멀라이즈를 이용해 흐린 영상의 화질 개선하기

import cv2
import numpy as np
import matplotlib.pylab as plt

img = cv2.imread("./img/abnormal.jpg", cv2.IMREAD_GRAYSCALE)

# 직접 정규화 연산
img_f = img.astype(np.float32)
img_norm = ((img_f - img_f.min()) * (255) / (img_f.max() - img_f.min()))
img_norm = img_norm.astype(np.uint8)

# OpenCV를 이용한 정규화 연산
# normalize(정규화 이전 데이터, 정규화 이후 데이터, 정규화 구간 1, 정규화 구간2, 알고리즘 선택 플래그 상수)
img_norm2 = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX)

# 히스토그램 계산
hist = cv2.calcHist([img], [0], None, [256], [0,255])
hist_norm = cv2.calcHist([img_norm], [0], None, [256], [0,255])
hist_norm2 = cv2.calcHist([img_norm2], [0], None, [256], [0,255])

cv2.imshow("Before", img)
cv2.imshow("Manual", img_norm)
cv2.imshow("cv2.normalize()", img_norm2)

hists = {"Before" : hist, "Manual" : hist_norm, "cv2.normalize()" : hist_norm2}
for i, (k,v) in enumerate(hists.items()):
    plt.subplot(1,3,i+1)    # 1,3 배열에 각각 히스토그램 순서대로 출력
    plt.title(k)
    plt.plot(v)
plt.show()