# 컬러 이미지에 대한 이퀄라이즈
# 어두운 이미지 개선 (명암 개선)

import cv2
from cv2 import COLOR_BGR2YUV
import numpy as np

img = cv2.imread("./img/yate.jpg")

# 컬러 스케일을 YUV로 변경
img_yuv = cv2.cvtColor(img, COLOR_BGR2YUV)

# equalizeHist(대상이미지)
img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])

img2 = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)

cv2.imshow("Before", img)
cv2.imshow("After", img2)
cv2.waitKey()
cv2.destroyAllWindows()