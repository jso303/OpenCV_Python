# 뒤틀기
# 어핀 변환

import cv2
import numpy as np
import matplotlib.pylab as plt

# imread에 직접적으로 영상 주소를 넣지 않고 간접적으로 삽입도 가능
file_name = "./img/fish.jpg"
img = cv2.imread(file_name)
rows, cols = img.shape[:2]

# 변환 전, 후 각 3개의 좌표 생성
pts1 = np.float32([[100,50], [200,50], [100,200]])
pts2 = np.float32([[80,70], [210,60], [250,120]])

# 변환전 좌표를 이미지에 점으로 표시
cv2.circle(img, (100,50), 5, (255,0), -1)       # 파랑점
cv2.circle(img, (200,50), 5, (0,255,0), -1)     # 녹색점
cv2.circle(img, (100,200), 5, (0,0,255), -1)    # 빨강점

# 짝 지은 3개의 좌표로 변환행렬 계산
# 전, 후 좌표 움직임 기준으로 이미지를 뒤틈
# mtrx = cv2.getAffineTransform(변환 전 좌표 3개(float32의 3x2 배열), 변환 후 좌표 3개(float32의 3x2 배열))
mtrx = cv2.getAffineTransform(pts1, pts2)
dst = cv2.warpAffine(img, mtrx, (int(cols*1.5), rows))

cv2.imshow("origin", img)
cv2.imshow("affin", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()