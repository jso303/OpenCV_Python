# 방사 왜곡 효과를 cv2.undistort로 구현

import cv2
import numpy as np

img = np.full((300, 400, 3), 255, np.uint8)
img[::10, :, :] = 0
img[:, ::10, :] = 0

width = img.shape[1]
height = img.shape[0]

k1, k2, p1, p2 = 0.001, 0, 0, 0         # 배럴 왜곡     # 밖으로 튀어나오는 왜곡
# k1, k2, p1, p2 = -0.0005, 0, 0, 0     # 핀쿠션 왜곡   # 안으로 들어가는 왜곡
distCoeff = np.float64([k1, k2, p1, p2])

# 임의의 값으로 카메라 매트릭스 설정
fx, fy = 10, 10
cx, cy = width/2, height/2
camMtx = np.float32([[fx, 0, cx], [0, fy, cy], [0,0,1]])

# 왜곡 변형
# cv2.undistort(입력 원본 영상, 카메라 매트릭스, 왜곡 계수)
# distCoeff = np.float64([k1, k2, p1, p2])
dst = cv2.undistort(img, camMtx, distCoeff) 

cv2.imshow("original", img)
cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()