# 샤르 필터
# 소벨 필터는 커널의 크기가 작거나 커널의 크기가 크더라도 중심에서 멀어지면
# 정확도가 떨어지는데 이를 개선한 필터다.

import cv2
import numpy as np

img = cv2.imread("./img/sudoku.jpg")

# 샤르 커널을 직접 생성해서 경계 검출
gx_k = np.array([[-3,0,3],[-10,0,10],[-3,0,3]])
gy_k = np.array([[-3,-10,-3],[0,0,0],[3,10,3]])
edge_gx = cv2.filter2D(img, -1, gx_k)
edge_gy = cv2.filter2D(img, -1, gy_k)

# 샤르 API로 경계 검출
# cv2.Scharr(입력 영상, 출력 영상 dtype, 미분차수(dx), 미분차수(dy))
scharrx = cv2.Scharr(img, -1,1,0)
scharry = cv2.Scharr(img, -1,0,1)

merged1 = np.hstack((img, edge_gx, edge_gy))
merged2 = np.hstack((img, scharrx, scharry))
merged = np.vstack((merged1, merged2))
cv2.imshow("Scharr", merged)
cv2.waitKey(0)
cv2.destroyAllWindows()