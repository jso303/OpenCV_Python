import matplotlib.pyplot as plt
import numpy as np
import cv2

img1 = cv2.imread("./img/Ch03_img/girl.jpg")
img2 = cv2.imread("./img/Ch03_img/boy.jpg")

plt.subplot(1,2,1)
plt.imshow(img1[:,:,(2,1,0)])       # :,;,(2,1,0) == :,:,::-1   # 같은 값임. rgb 색 적용 순서 지정
plt.xticks([])                      # x축 눈금 제거
plt.yticks([])                      # y축 눈금 제거

plt.subplot(1,2,2)
plt.imshow(img2[:,:,::-1])
plt.xticks([])
plt.yticks([])

plt.show()