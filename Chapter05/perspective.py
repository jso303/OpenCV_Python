# 원근변환

import cv2
import numpy as np

img = cv2.imread("./img/fish.jpg")
rows, cols = img.shape[:2]
# rows = img 세로 좌표 최대 값, cols = img 가로 좌표 최대 값
# 0,0 = 왼쪽 위 모서리, cols,rows = 오른쪽 아래 모서리

# 원근 변환 전후 4개 좌표
pts1 = np.float32([[0,0],[0,rows], [cols,0], [cols,rows]])
pts2 = np.float32([[100,50], [10,rows-50], [cols-100, 50], [cols-10, rows-50]])

# 좌표를 원본 이미지에 원으로 표시
cv2.circle(img, (0,0), 10, (255,0,0), -1)           # 파랑
cv2.circle(img, (0,rows),10,(0,255,0), -1)          # 초록
cv2.circle(img, (cols,0), 10, (0,0,255), -1)        # 빨강
cv2.circle(img, (cols,rows), 10, (0,255,255), -1)   # 노랑

# 원근 변환행렬 계산
mtrx = cv2.getPerspectiveTransform(pts1, pts2)

# 원근 변환 적용
dst = cv2.warpPerspective(img,mtrx, (cols,rows))

cv2.imshow("origin", img)
cv2.imshow("perspective", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()