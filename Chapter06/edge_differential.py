# 미분 커널로 경계 검출
# 배경과 전경을 분리하는데 사용
# 픽셀 값의 변화가 갑자기 크게 일어나는 지점 검출

import cv2
import numpy as np

img = cv2.imread("./img/sudoku.jpg")

gx_kernel = np.array([[-1, 1]])
gy_kernel = np.array([[-1], [1]])

edge_gx = cv2.filter2D(img, -1, gx_kernel)
edge_gy = cv2.filter2D(img, -1, gy_kernel)

merged = np.hstack((img, edge_gx, edge_gy))
cv2.imshow("edge", merged)
cv2.waitKey(0)
cv2.destroyAllWindows()