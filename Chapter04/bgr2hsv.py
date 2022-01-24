# HSV 컬러 스페이스로 변환하기
# H(Hue : 색조), S(Saturation : 채도), V(Value : 명도)
# 원통형 시스템 사용 (원통 각:H, 원통 반지름:S, 원통 높이:V)

import cv2
import numpy as np

red_bgr = np.array([[[0,0,255]]], dtype=np.uint8)           # 빨강 값만 갖는 픽셀
green_bgr = np.array([[[0,255,0]]], dtype=np.uint8)         # 초록 값만 갖는 픽셀
blue_bgr = np.array([[[255,0,0]]], dtype=np.uint8)          # 파랑 값만 갖는 픽셀
yellow_bgr = np.array([[[0,255,255]]], dtype=np.uint8)      # 노랑 값만 갖는 픽셀

# BGR 컬러 스페이스를 HSV 컬러 스페이스로 변환
red_hsv = cv2.cvtColor(red_bgr, cv2.COLOR_BGR2HSV)
green_hsv = cv2.cvtColor(green_bgr, cv2.COLOR_BGR2HSV)
blue_hsv = cv2.cvtColor(blue_bgr, cv2.COLOR_BGR2HSV)
yellow_hsv = cv2.cvtColor(yellow_bgr, cv2.COLOR_BGR2HSV)

print("red", red_hsv)
print("green", green_hsv)
print("blue", blue_hsv)
print("yellow", yellow_hsv)
