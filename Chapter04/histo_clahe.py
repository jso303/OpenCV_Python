# CLAHE : 영상 전체에 이퀄라이즈를 적용하였을 때 너무 밝은 부분이 날아가는 현상을 막기 위해
# 영상을 여러 영역으로 나누어 이퀄라이즈를 적용하는것

import cv2
import numpy as np
import matplotlib.pylab as plt

img = cv2.imread("./img/bright.jpg")
img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

# 밝기 채널에 대해서 이퀄라이즈 적용
img_eq = img_yuv.copy()
img_eq[:,:,0] = cv2.equalizeHist(img_eq[:,:,0])
img_eq = cv2.cvtColor(img_eq, cv2.COLOR_YUV2BGR)

# 밝기 채널에 대해서 CLAHE 적용
img_clahe = img_yuv.copy()

# createCLAHE(Contrast 제한 경계 값= 3.0, 영역 크기 = (8 x 8))
clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
img_clahe[:,:,0] = clahe.apply(img_clahe[:,:,0])
img_clahe = cv2.cvtColor(img_clahe, cv2.COLOR_YUV2BGR)

cv2.imshow("Before", img)
cv2.imshow("CLAHE", img_clahe)
cv2.imshow("equalizeHist", img_eq)
cv2.waitKey()
cv2.destroyAllWindows()