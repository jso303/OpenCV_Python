# 이미지 단순 합성

import cv2
from matplotlib.pyplot import xticks
import numpy as np
import matplotlib.pylab as plt

img1 = cv2.imread("./img/wing_wall.jpg")
img2 = cv2.imread("./img/yate.jpg")

# 단순 값 더하기, 화소가 고르지 못하고 255를 초과한 부분은 이상한 색을 띔
img3 = img1 + img2
# 대부분 픽셀 값이 255 가까이 몰려 하얗게 보임
img4 = cv2.add(img1, img2)      

imgs = {"img1":img1, "img2":img2, "img1+img2":img3, "cv2.add(img1, img2)":img4}

for i, (k,v) in enumerate(imgs.items()):
    plt.subplot(2,2,i+1)
    plt.imshow(v[:,:,::-1])
    plt.title(k)
    plt.xticks([])
    plt.yticks([])
plt.show()