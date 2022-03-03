# 확률적 허프 선 변환
# 허프 선 검출은 모든 점에 대해 수많은 선을 그어 직선을 검출하기 때문에 연산이 많이 필요함
# 이를 개선하여 무작위의 픽셀에 대하여 허프 변환을 수행하여 적은 연산으로 처리
# 기본 허프 선 검출에 비해 검출이 적게 되므로 edge를 강하게 하고 threshold를 낮게 지정한다.

import cv2
import numpy as np

img = cv2.imread("./img/sudoku.jpg")
img2 = img.copy()

imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(imgray, 50, 200)

# cv2.HoughLinesP(입력 영상, 거리 측정 해상도, 각도 측정 해상도, \
# 직선으로 판단할 최소한의 동일 픽셀 개수(threshold), 검출 결과 배열,\
# 선으로 인정할 최소 길이, 선으로 판단할 최대 간격)
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 10, None, 20, 2)
for line in lines:
    # 검출된 선 그리기(녹색)
    x1, y1, x2, y2 = line[0]
    cv2.line(img2, (x1, y1), (x2, y2), (0,255,0), 1)

merged = np.hstack((img, img2))
cv2.imshow("Probability hough line", merged)
cv2.waitKey()
cv2.destroyAllWindows()