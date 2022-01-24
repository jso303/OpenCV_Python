import cv2
import numpy as np

img = np.zeros((120,120,3), dtype=np.uint8)
img[25:35, :] = [255,0,0]   # 파
img[55:65, :] = [0,255,0]   # 녹
img[85:95, :] = [0,0,255]   # 빨

img[:, 35:45] = [255,255,0] # 파+녹 = 하늘색
img[:, 75:85] = [255,0,255] # 파+빨 = 분홍색

cv2.imshow('BGR', img)
cv2.waitKey(0)
cv2.destroyAllWindows()