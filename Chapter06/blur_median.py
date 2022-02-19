# 미디언 블러링
# 잡음 제거에 효과적

import cv2
import numpy as np

img = cv2.imread("./img/salt_pepper_noise.jpg")

# cv2.medianBlur(입력 영상, 커널 크기)
blur = cv2.medianBlur(img, 5)

merged = np.hstack((img, blur))
cv2.imshow("media", merged)
cv2.waitKey(0)
cv2.destroyAllWindows()