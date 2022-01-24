import cv2
import matplotlib.pyplot as plt

img = cv2.imread("./img/Ch03_img/girl.jpg")

plt.imshow(img)
plt.show()

# 색이 이상하게 나온다
# plt는 색을 RGB 순으로 해석하나
# opencv는 색을 BGR 순으로 만들어뒀기 때문
