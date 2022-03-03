# 영상 분할

# 컨투어 찾기와 그리기
# 컨투어 == 경계선, 외각선

import cv2
import numpy as np

img = cv2.imread("./img/shapes.png")
img2 = img.copy()

imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, imthres = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY_INV)

# cv2.findContours(입력이미지, 외각선 검출 모드, 외각선 근사화 방식)
# VS Code의 최신버전의 경우 아래의 교재 원문과 달리 im2를 적지 않아야 처리가 됨
# im2, contour, hierarchy = cv2.findContours(imthres, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)


# 가장 바깥쪽 컨투어에 대해 모든 좌표 반환
contour, hierarchy = cv2.findContours(imthres, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
# 가장 바깥쪽 컨투어에 대해 꼭지점 좌표만 반환
contour2, hierarchy = cv2.findContours(imthres, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print("도형의 개수: %d(%d)" %(len(contour), len(contour2)))

# 모든 좌표를 갖는 컨투어 그리기, 초록색
# cv2.drawContours(입력 영상, 그림 그릴 컨투어 배열, 그림 그릴 컨투어 인덱스(-1 은 모든 컨투어)\
#                  색상값, 선 두께)
cv2.drawContours(img, contour, -1, (0,255,0), 4)
# 꼭지점 좌표만을 갖는 컨투어 그리기, 초록색
cv2.drawContours(img2, contour2, -1, (0,255,0), 4)

# 컨투어의 모든 좌표를 작은 파란색 점(원)으로 표시
for i in contour:
    for j in i:
        cv2.circle(img, tuple(j[0]), 1, (255,0,0), -1)

# 컨투어의 꼭지점 좌표를 작은 파랑색 점(원)으로 표시        
for i in contour2:
    for j in i:
        cv2.circle(img2, tuple(j[0]), 3, (255,0,0), -1)
        
cv2.imshow("CHAIN_APPROX_NONE", img)
cv2.imshow("CHAIN_APPROX_SIMPLE", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()        