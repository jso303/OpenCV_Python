# 라플라시안 필터
# 두번 경계 검출을 하여 선명함
# 노이즈에 민감하므로 사전에 가우시안 필터로 노이즈를 제거하는게 좋음

import cv2
import numpy as np

# 라플라시안 필터 적용
img = cv2.imread("./img/sudoku.jpg")

# cv2.Laplacian(입력 영상, 출력영상 dtype)
edge = cv2.Laplacian(img, -1)

merged = np.hstack((img, edge))
cv2.imshow("Laplacian", merged)
cv2.waitKey(0)
cv2.destroyAllWindows()