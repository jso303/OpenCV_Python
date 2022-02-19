# 소벨 필터
# 수평, 수직, 대각선 검출에 모두 강함
# 실무에서 실질적으로 사용되는 필터

import cv2
import numpy as np

img = cv2.imread("./img/sudoku.jpg")

# 소벨 커널을 직접 생성해서 경계 검출
gx_k = np.array([[-1,0,1], [-2,0,2], [-1,0,1]])
gy_k = np.array([[-1,-2,-1], [0,0,0], [1,2,1]])

edge_gx = cv2.filter2D(img, -1, gx_k)
edge_gy = cv2.filter2D(img, -1, gy_k)

# 소벨 API로 경계 검출
# cv2.Sobel(입력 영상, 출력영상의 dtype, 미분차수 dx, 미분차수 dy, 커널의 크기 ksize)
sobelx = cv2.Sobel(img, -1, 1, 0, ksize=3)
sobely = cv2.Sobel(img, -1, 0, 1, ksize=3)

merged1 = np.hstack((img, edge_gx, edge_gy, edge_gx+edge_gy))
merged2 = np.hstack((img, sobelx, sobely, sobelx+sobely))
merged = np.vstack((merged1, merged2))
cv2.imshow("soble", merged)
cv2.waitKey(0)
cv2.destroyAllWindows()