# 시-토마시 코너 검출
# 해리스 코너 검출을 개선한 알고리즘
# 객체 추적에 좋은 특징이 됨

import cv2
import numpy as np

img = cv2.imread("./img/house.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 시-토마스의 코너 검출 매소드
# cv2.goodFeaturesToTrack(입력 영상, 얻고 싶은 코너 개수, 코너로 판단할 스레시 홀드 값,\
#                         코너 간 최소 거리)
corners = cv2.goodFeaturesToTrack(gray, 80, 0.01, 10)
corners = np.int32(corners)

# 검출된 좌표에 빨간색 동그라미 표시
for corner in corners:
    x,y = corner[0]
    cv2.circle(img, (x,y), 5, (0,0,255), 1, cv2.LINE_AA)

cv2.imshow("Corners", img)
cv2.waitKey()
cv2.destroyAllWindows()