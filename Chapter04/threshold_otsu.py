# 오츠의 이진화 알고리즘

# 글씨와 그림을 가장 잘 얻을 수 있는 경계 값을 반복적 시도 없이
# 한번에 효율적으로 찾는 방법

import cv2
import numpy as np
import matplotlib.pylab as plt

img = cv2.imread("./img/scaned_paper.jpg", cv2.IMREAD_GRAYSCALE)

# 경계 값 130을 기준으로 바이너리 이미지 생성
_, t_130 = cv2.threshold(img, 130, 255, cv2.THRESH_BINARY) 
# 오츠의 알고리즘을 이용해 최적의 경계 값으로 바이너리 이미지 생성     
t, t_otsu = cv2.threshold(img, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)    
print("otsu threshold:", t) # 최적의 경계 값 수치 출력

imgs = {"Original":img, "t:130":t_130, "otsu:%d"%t: t_otsu}
for i, (key, value) in enumerate(imgs.items()):
    plt.subplot(1,3,i+1)    # 1행3열에서 순서대로
    plt.title(key)
    plt.imshow(value, cmap="gray")
    plt.xticks([])
    plt.yticks([])
    
plt.show()