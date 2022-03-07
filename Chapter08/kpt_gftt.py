# GFTTDetector로 키 포인트 검출

import cv2
import numpy as np

img = cv2.imread("./img/house.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Good feature to trac 검출기 생성
gftt = cv2.GFTTDetector_create()
# 키 포인트 검출
keypoints = gftt.detect(gray, None)
# 키 포인트 그리기
# cv2.drawKeyPoints(입력 이미지, 표시할 키 포인트 리스트, 키 포인트가 그려진 결과 이미지, \
#                   표시할 색상(기본값: 랜덤))
img_draw = cv2.drawKeypoints(img, keypoints, None)

cv2.imshow("GFTTDectector", img_draw)
cv2.waitKey(0)
cv2.destroyAllWindows()