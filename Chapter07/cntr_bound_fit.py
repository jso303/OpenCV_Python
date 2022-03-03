# 컨투어를 감싸는 도형 그리기

import cv2
import numpy as np

img = cv2.imread("./img/lightning.png")
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, th = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY_INV)

# 컨투어 찾기
contours, hr = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contr = contours[0]

# 좌표를 감싸는 사각형 구하기
x,y,w,h = cv2.boundingRect(contr)
# 검은색으로 표시
cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,0), 3)

# 최소한의 사각형 표시
rect = cv2.minAreaRect(contr)
# 중심점과 각도를 4개의 꼭지점 좌표로 변환
box = cv2.boxPoints(rect)
# 정수로 변환
box = np.int0(box)
# 최소한의 사각형 이미지에 그리기(초록색)
cv2.drawContours(img, [box], -1, (0,255,0), 3)

# 최소한의 원 표시(파란색)
(x,y), radius = cv2.minEnclosingCircle(contr)
cv2.circle(img, (int(x), int(y)), int(radius), (255,0,0), 2)

# 최소한의 삼각형 표시(분홍색)
ret, tri = cv2.minEnclosingTriangle(contr)
cv2.polylines(img, [np.int32(tri)], True, (255,0,255), 2)

# 최소한의 타원 표시(노란색)
ellipse = cv2.fitEllipse(contr)
cv2.ellipse(img, ellipse, (0,255,255), 3)

# 중심점을 통과하는 직선 표시(빨간색)
[vx, vy, x,y] = cv2.fitLine(contr, cv2.DIST_L2,0,0.01,0.01)
cols, rows = img.shape[:2]
# 기존 교제에서는 int를 씌우지 않고 사용하여 type 오류가 나옴
lefty = int(0-x*(vy/vx) + y)
righty = int((cols-x)*(vy/vx) + y)
cv2.line(img, (0, lefty), (cols-1, righty), (0,0,255), 2)
    
cv2.imshow("Bound Fit shapes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()