# 캐니 엣지 검출
# 4단계의 알고리즘을 적용한 엣지 검출기

# 1단계 : 노이즈 제거(가우시안 블러링 필터 사용)
# 2단계 : 엣지 그레디언트 방향 계산(소벨 마스크로 검출)
# 3단계 : 비최대치 억제(그레디언트 방향에서 검출된 엣지 중 가장 큰 값 선택 후 나머지 제거)
# 4단계 : 이력 스레시홀딩(두 개의 경계 값을 지정하고 경계 값 내의 연결성을 지닌 엣지만 선택)

import cv2
import numpy as np

img = cv2.imread("./img/sudoku.jpg")

# cv2.Canny(입력영상, 이력 스레시홀딩에 사용할 최소 값, 최대 값)
edges = cv2.Canny(img,100,200)

cv2.imshow("Original", img)
cv2.imshow("Canny", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()