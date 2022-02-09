# 평행 이동

# cv2.warpAffine(원본영상, 변환행렬, 결과이미지크기, 결과이미지, 보간법 알고리즘 선택,\
# 외곽 영역 보정 선택, 외각 영역 보정이 cv2.BORDER_CONSTANT 일 경우 사용할 색상 값)

import cv2
import numpy as np

img = cv2.imread("./img/fish.jpg")
rows,cols = img.shape[0:2]          # 영상의 크기

dx, dy = 100, 50                    # 이동할 픽셀의 거리

# 변환행렬 생성
mtrx = np.float32([[1,0,dx], [0,1,dy]])

# 단순 이동
dst = cv2.warpAffine(img, mtrx, (cols+dx, rows+dy))
# 이동 후 탈락된 외각 픽셀을 파란색으로 보정
dst2 = cv2.warpAffine(img, mtrx, (cols+dx, rows+dy), None,\
                        cv2.INTER_LINEAR, cv2.BORDER_CONSTANT, (255,0,0))
# 탈락된 외곽 픽셀을 원본을 반사시켜 보정(BORDER_REFLECT)
dst3 = cv2.warpAffine(img, mtrx, (cols+dx, rows+dy), None,\
                        cv2.INTER_LINEAR, cv2.BORDER_REFLECT)

cv2.imshow("original", img)
cv2.imshow("trans", dst)
cv2.imshow("BORDER_CONSTATNT", dst2)
cv2.imshow("BORDER_FEFLECT", dst3)
cv2.waitKey(0)
cv2.destroyAllWindows()