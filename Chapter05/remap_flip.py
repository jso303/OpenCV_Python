# 영상 뒤집기

import cv2
import numpy as np
import time

img = cv2.imread("./img/girl.jpg")
rows, cols = img.shape[:2]

# 행렬 변환으로 뒤집기 구현
st = time.time()
mflip = np.float32([[-1, 0, cols-1],[0,-1,rows-1]])
fliped1 = cv2.warpAffine(img, mflip, (cols, rows))
print("matrix:", time.time()-st)

# OpenCV의 remap 함수로 뒤집기 구현

# cv2.remap(입력영상, x축으로 이동할 좌표(인덱스), y축으로 이동할 좌표(인덱스), \
# 결과이미지, 보간법 알고리즘 선택, 외곽 영역 보정 선택, \
# 외각 영역 보정이 cv2.BORDER_CONSTANT 일 경우 사용할 색상 값))

st2 = time.time()
mapy, mapx = np.indices((rows, cols), dtype=np.float32)
mapx = cols - mapx -1       # x축 좌표 뒤집기 연산
mapy = rows - mapy -1       # y축 좌표 뒤집기 연산
fliped2 = cv2.remap(img, mapx, mapy, cv2.INTER_LINEAR)
print("remap:", time.time()-st2)

cv2.imshow("origin", img)
cv2.imshow("fliped1", fliped1)
cv2.imshow("fliped2", fliped2)
cv2.waitKey()
cv2.destroyAllWindows()

