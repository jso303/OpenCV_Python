# 어둡게 나온 사진을 이퀄라이즈를 이용하여 개선시키는 방법

import cv2
import numpy as np
import matplotlib.pylab as plt

img = cv2.imread("./img/yate.jpg", cv2.IMREAD_GRAYSCALE)
rows, cols = img.shape[:2]

# 이퀄라이즈 직접 연산
hist = cv2.calcHist([img], [0], None, [256], [0,256])       # 히스토그램 계산
cdf = hist.cumsum()                                         # 누적 히스토그램
cdf_m = np.ma.masked_equal(cdf,0)                           # 0(zero)인 값을 NaN으로 제거
cdf_m = (cdf_m - cdf_m.min())/(rows * cols) * 255           # 이퀄라이즈 히스토그램 계산
cdf = np.ma.filled(cdf_m,0).astype("uint8")                 # NaN을 다시 0으로 환원
img2 = cdf[img]                                             # 히스토그램을 픽셀로 매칭

# OpenCV API로 이퀄라이즈 연산
img3 = cv2.equalizeHist(img)

# 이퀄라이즈 결과 히스토그램 계산
hist2 = cv2.calcHist([img2], [0], None, [256], [0,256])
hist3 = cv2.calcHist([img3], [0], None, [256], [0,256])

cv2.imshow("Before", img)
cv2.imshow("Manual", img2)
cv2.imshow("cv2.equalizeHist()", img3)
hists = {"Before":hist, "Manual":hist2, "cv2.equalizeHist()":hist3}
for i, (k,v) in enumerate(hists.items()):
    plt.subplot(1,3,i+1)
    plt.title(k)
    plt.plot(v)
plt.show()
