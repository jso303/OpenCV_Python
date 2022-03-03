# 허프 선 검출
# 영상에서 직선과 원 같은 간단한 모양 식별


import cv2
import numpy as np

img = cv2.imread("./img/sudoku.jpg")
img2 = img.copy()
h, w = img.shape[:2]

imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.Canny(입력 영상, 엣지 검출 경계 최소값, 최대값)
edges = cv2.Canny(imgray, 100, 200)

# 허프 선 검출
# cv2.HoughLines(입력영상, 거리측정 해상도, 각도 측정 해상도,\
# 직선으로 판단할 최소한의 동일 픽셀(threshold) 개수)
lines = cv2.HoughLines(edges, 1, np.pi/180, 130)
for line in lines:          # 검출 된 선 모두 순회
    r, theta = line[0]      # 거리와 각도
    tx, ty = np.cos(theta), np.sin(theta)   # x,y 축에 대한 삼각비
    x0, y0 = tx*r, ty*r                     # x,y 기준 절편 좌표
    # 기준 좌표에 빨간색 점 그리기
    cv2.circle(img2, (int(abs(x0)), int(abs(y0))), 3, (0,0,255), -1)
    
    x1, y1 = int(x0 + w*(-ty)), int(y0 + h * tx)
    x2, y2 = int(x0 - w*(-ty)), int(y0 - h * tx)
    
    cv2.line(img2, (x1, y1), (x2, y2), (0,255,0), 1)
    
merged = np.hstack((img, img2))
cv2.imshow("hough line", merged)
cv2.waitKey()
cv2.destroyAllWindows()