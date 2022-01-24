import cv2
import matplotlib.pyplot as plt

img = cv2.imread("./img/Ch03_img/girl.jpg")

plt.imshow(img[:,:,::-1])   # 이미지 컬러 채널 변경
plt.xticks([])              # x 축 눈금 제거
plt.yticks([])              # y 축 눈금 제거
plt.show()