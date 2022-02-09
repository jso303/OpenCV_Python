# 직접 변환행렬을 생성하여 회전 하기

import cv2
import numpy as np

img = cv2.imread("./img/fish.jpg")
rows,cols = img.shape[0:2]

# 라디안 각도 계산
d45 = 45.0 * np.pi / 180    # 45도
d90 = 90.0 * np.pi / 180    # 90도

# 회전을 위한 변환행렬 생성
m45 = np.float32([[np.cos(d45), -1*np.sin(d45), rows//2], [np.sin(d45), \
                  np.cos(d45), -1*cols//4]])
m90 = np.float32([[np.cos(d90), -1*np.sin(d90), rows], [np.sin(d90), \
                   np.cos(d90), 0]])

# 회전 변환행렬 적용
# 탈락된 외각 픽셀 초록색으로 보정
r45 = cv2.warpAffine(img, m45, (cols,rows),None, cv2.INTER_LINEAR, cv2.BORDER_CONSTANT, (0,255,0))
r90 = cv2.warpAffine(img, m90, (rows,cols))

cv2.imshow("origin", img)
cv2.imshow("45", r45)
cv2.imshow("90", r90)
cv2.waitKey(0)
cv2.destroyAllWindows()
