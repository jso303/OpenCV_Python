# 컬러 히스토그램

import cv2
import numpy as np
import matplotlib.pylab as plt

img = cv2.imread("./img/mountain.jpg")
cv2.imshow("img", img)

channels = cv2.split(img)
colors = ("b", "g", "r")
for (ch, color) in zip (channels, colors):
    hist = cv2.calcHist([ch], [0], None, [256], [0,256])
    plt.plot(hist, color = color)
plt.show()