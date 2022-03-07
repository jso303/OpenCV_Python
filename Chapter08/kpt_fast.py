# 속도를 개선한 알고리즘

# 코너 검출 시 미분 연산으로 엣지 검출을 하지 않고 픽셀 중심으로 주변 픽셀의 값이 중심 픽셀보다
# 임계 값 이상 밝거나 어두운 것이 특정 개수 이상 연속되면 코너로 판단

import cv2
import numpy as np

img = cv2.imread("./img/house.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# FAST 특징 검출기 생성
fast = cv2.FastFeatureDetector_create(50)   # 코너 판단 임계 값 50

keypoints = fast.detect(gray, None)
img = cv2.drawKeypoints(img, keypoints, None)

cv2.imshow("FAST", img)
cv2.waitKey()
cv2.destroyAllWindows()