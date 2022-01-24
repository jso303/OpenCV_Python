import cv2
import numpy as np

img = np.zeros((120,120), dtype=np.uint8)   # 120X120 2차원 배열 생성, 0 값을 지님 = 검은색

img[25:35, :] = 45                          # 25~35행 모든 열에 45 할당
img[55:65, :] = 115                         # 55~65행 모든 열에 115 할당
img[85:95, :] = 160                         # 85~95행 모든 열에 160 할당

img[:, 35:45] = 205                         # 모든 행 35~45열에 205 할당
img[:, 75:85] = 255                         # 모든 행 75~85열에 255 할당

# 뒤에 적용하는 값이 기존 값을 덮음.

cv2.imshow('Gray', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
