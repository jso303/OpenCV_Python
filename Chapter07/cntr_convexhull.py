# 볼록 선체
# 어느 한 부분도 오목하지 않은 상태
# 객체의 외각 영역을 찾는데 사용


import cv2
import numpy as np

img = cv2.imread("./img/hand.jpg")
img2 = img.copy()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, th = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

# 컨투어 찾기
contours, heiarchy = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 컨투어 그리기
cntr = contours[0]
cv2.drawContours(img, [cntr], -1, (0,255,0), 1)

# 볼록 선체 찾기(좌표 기준)와 그리기
# cv2.convexHull(입력 컨투어)
hull = cv2.convexHull(cntr)
cv2.drawContours(img2, [hull], -1, (0,255,0), 1)
# cv2.isContourConvex(볼록 선체 만족)   # True 볼록 선체 만족(오목 없음), False 불만족(오목 존재)
print(cv2.isContourConvex(cntr), cv2.isContourConvex(hull))

# 볼록 선체 찾기(인덱스 기준)
# cv2.convexHull(입력컨투어, 결과 좌표 형식 선택(True : 볼록 선체 좌표 반환, False : 입력 컨투어 중 볼록 선체에 해당하는 인덱스 반환))
hull2 = cv2.convexHull(cntr, returnPoints=False)
# cv2.convexityDefects(입력컨투어, 볼록 선체에 해당하는 컨투어 인덱스)
defects = cv2.convexityDefects(cntr, hull2)

# 볼록 선체 결함 순회
for i in range(defects.shape[0]):
    # 시작, 종료, 가장 먼 지점, 거리
    startP, endP, farthestP, distance = defects[i, 0]
    # 가장 먼 지점의 좌표 구하기
    farthest = tuple(cntr[farthestP][0])
    # 거리를 부동 소수점으로 변환
    dist = distance/256.0
    
    # 거리가 1보다 큰 경우
    if dist>1:
        # 빨간색 점으로 표시
        cv2.circle(img2, farthest, 3, (0,0,255), -1)
        
cv2.imshow("contour", img)
cv2.imshow("convex hull", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()