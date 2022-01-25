# 바이너리 이미지 만들기 (0과 255만으로 이루어진 이미지)

from multiprocessing.sharedctypes import Value
import cv2
import numpy as np
import matplotlib.pylab as plt

img = cv2.imread("./img/gray_gradient.jpg", cv2.IMREAD_GRAYSCALE)

thresh_np = np.zeros_like(img)  # 원본과 동일한 크기의 0으로 채워진 이미지
thresh_np [ img > 127 ] = 255   # 127보다 큰 값은 255로 변경

ret, thresh_cv = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
print(ret)

# 원본 / Numpy로 바이너리 처리 / Open CV로 바이너리 처리
imgs = {"Original": img, "NumPy API": thresh_np, "cv2.threshold":thresh_cv}
for i, (key, value) in enumerate(imgs.items()):
    plt.subplot(1,3,i+1)        # 1행 3열에서 i+1 번째 배치 == for 문으로 각각 1,2,3 번째 배치
    plt.title(key)              # 그래프의 타이틀("Original", "NumPy API", "cv2.threshold")
    plt.imshow(value, cmap="gray")  # 그래프의 값, 컬러맵="gray" 로 출력
    plt.xticks([])              # x축 눈금 제거
    plt.yticks([])              # y축 눈금 제거
    
plt.show()