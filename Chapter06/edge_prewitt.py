# 프리웟 필터
# 각 방향으로 차분을 세번 계산하여 경계가 선명함
# 대각선 검출은 약함

import cv2
import numpy as np

file_name = "./img/sudoku.jpg"
img = cv2.imread(file_name)

gx_k = np.array([[-1,0,1], [-1,0,1], [-1,0,1]])
gy_k = np.array([[-1,-1,-1], [0,0,0],[1,1,1]])

edge_gx = cv2.filter2D(img, -1, gx_k)
edge_gy = cv2.filter2D(img, -1, gy_k)

merged = np.hstack((img, edge_gx, edge_gy, edge_gx+edge_gy))
cv2.imshow("prewitt corss", merged)
cv2.waitKey(0)
cv2.destroyAllWindows()