# SimpleBlobDetector 검출기
# 자잘한 객체는 노이즈로 판단하고 큰 객체만 검출

import cv2
import numpy as np

img = cv2.imread("./img/house.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# SimpleBlobDetector 생성
detector = cv2.SimpleBlobDetector_create()
keypoints = detector.detect(gray)
img = cv2.drawKeypoints(img, keypoints, None, (0,0,255),\
                        flags = cv2.DrawMatchesFlags_DRAW_RICH_KEYPOINTS)

cv2.imshow("Blob", img)
cv2.waitKey(0)