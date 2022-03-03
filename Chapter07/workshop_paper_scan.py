# 문서 스캐너
# 경계 검출한 후 가장 큰 컨투어를 찾아 꼭지점 4개를 구함
# 이후 꼭지점 상하좌우를 찾은 뒤 좌표의 폭과 너비를 동일하게 조정
# 원근 변환으로 스캔모양을 만듬

import cv2
import numpy as np

# 기본 이미지
img = cv2.imread("./img/paper.jpg")
cv2.imshow("original", img)
cv2.waitKey(0)
draw = img.copy()

# 그레이 스케일로 변환, 노이즈 제거, 경계 검출
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (3,3), 0)
edged = cv2.Canny(gray, 75, 200)
cv2.imshow("scan", edged)
cv2.waitKey(0)

# 컨투어 찾기
cnts, _ = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 컨투어 그리기
cv2.drawContours(draw, cnts, -1, (0,255,0))
cv2.imshow("scan", draw)
cv2.waitKey(0)

# 컨투어들 중에 영역 크기순으로 정렬
# 꼭지점 찾는 작업
cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:5]
for c in cnts:
    # 영역이 가장 큰 컨투어부터 근사 컨투어 단순화
    peri = cv2.arcLength(c, True)
    # 둘레 길이의 0.02 근사 값으로 근사화
    vertices = cv2.approxPolyDP(c, 0.02*peri, True)
    # 근사 꼭지점이 4개면 중지
    if len(vertices) == 4:
        break
pts = vertices.reshape(4,2)
# 꼭지점 판단된 좌표에 초록색 동그라미 표시
for x,y in pts:
    cv2.circle(draw, (x,y), 10, (0,255,0), -1)
cv2.imshow("scan", draw)
cv2.waitKey(0)

# 좌표 4개 중 상하좌우 찾기
sm = pts.sum(axis = 1)
diff = np.diff(pts, axis = 1)

topLeft = pts[np.argmin(sm)]        # x+y 값이 가장 작은 값이 좌상단
bottomRight = pts[np.argmax(sm)]    # x+y 값이 가장 큰 값이 우하단
topRight = pts[np.argmin(diff)]     # x-y 값이 가장 작은 값이 우상단
bottomLeft = pts[np.argmax(diff)]   # x-y 값이 가장 큰 값이 좌하단

pts1 = np.float32([topLeft, topRight, bottomRight, bottomLeft])

 # 변환 후 영상에 사용될 서류의 폭과 높이 계산
# 좌우 값 차이 중 큰 값으로 폭
# 상하 값 차이 중 큰 값으로 높이
# [0] : x 좌표(폭 계산에 사용), [1] : y 좌표(높이 계산에 사용)
w1 = abs(bottomRight[0] - bottomLeft[0])    # 상단 좌우 좌표간의 거리
w2 = abs(topRight[0] - topLeft[0])          # 하당 좌우 좌표간의 거리
h1 = abs(topRight[1] - bottomRight[1])      # 우측 상하 좌표간의 거리
h2 = abs(topLeft[1] - bottomLeft[1])        # 좌측 상하 좌표간의 거리
width = max([w1, w2])                       # 두 좌우 거리간의 최대값이 서류의 폭
height = max([h1, h2])                      # 두 상하 거리간의 최대값이 서류의 높이
            
# 변환 후 4개 좌표
pts2 = np.float32([[0,0], [width-1, 0], [width-1, height-1], [0, height-1]])
            
# 변환 행렬 계산
mtrx = cv2.getPerspectiveTransform(pts1, pts2)
            
# 원근 변환으로 폭, 높이를 동일한 수준으로 맞춰줌
# 타입 오류가 나오는 폭, 높이 값에 int를 씌워주어 해결
result = cv2.warpPerspective(img, mtrx, (int(width), int(height)))
cv2.imshow("scan", result)
cv2.waitKey(0)
cv2.destroyAllWindows()