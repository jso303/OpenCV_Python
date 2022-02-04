# 투명 배경 PNG 파일을 이용한 합성

import cv2
import numpy as np

img_fg = cv2.imread("./img/opencv_logo.png", cv2.IMREAD_UNCHANGED)
img_bg = cv2.imread("./img/girl.jpg")

# 알파 채널을 이용해 마스크와 역마스크 생성 
# 마스크 : 1을 넘는 값(검은색이 아닌 값)을 255(흰색)으로 바꿈
_, mask = cv2.threshold(img_fg[:,:,3], 1, 255, cv2.THRESH_BINARY)
# 역마스크 : 마스크의 반대값 (255 <-> 0)
mask_inv = cv2.bitwise_not(mask)

# 전경 영상 크기로 배경 영상에서 ROI(관심영역) 잘라내기
img_fg = cv2.cvtColor(img_fg, cv2.COLOR_BGRA2BGR)   # 그레이 스케일을 BGR 스케일로 변환
h, w = img_fg.shape[:2]             # img_fg의 크기 추출 (h : 높이, w : 너비)
roi = img_bg[10:10+h, 10:10+w]      # girl.jpg에서 로고가 위치할 부분 img_fg 크기만큼 지정

# 마스크를 이용해서 오려내기
masked_fg = cv2.bitwise_and(img_fg, img_fg, mask=mask)  # 전경 : 주 대상
masked_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)    # 배경 : 나머지

added = masked_fg + masked_bg       # 전경 배경 합성
img_bg[10:10+h, 10:10+w] = added    # img_bg(girl.jpg) 이미지의 관심영역에 added 이미지 덧씌우기

cv2.imshow("mask", mask)
cv2.imshow("mask_inv", mask_inv)
cv2.imshow("masked_fg", masked_fg)
cv2.imshow("masked_bg", masked_bg)
cv2.imshow("added", added)
cv2.imshow("result", img_bg)
cv2.waitKey()
cv2.destroyAllWindows()