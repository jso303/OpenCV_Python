# 컨투어 계층 트리
# 도형 안의 도형 모양에서 컨투어를 계층 정보로 수집하기

import cv2
import numpy as np

img = cv2.imread("./img/shapes_donut.png")
img2 = img.copy()

imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, imthres = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY_INV)

# 가장 바깥 컨투어만 수집
contour, hierarchy = cv2.findContours(imthres, cv2.RETR_EXTERNAL, \
                                           cv2.CHAIN_APPROX_NONE)
# 컨투어 개수와 계층 트리 출력
print(len(contour), hierarchy)

# 모든 컨투어를 트리 계층으로 수집
contour2, hierarchy = cv2.findContours(imthres, cv2.RETR_TREE,\
                                            cv2.CHAIN_APPROX_SIMPLE)
# 컨투어 개수와 계층 트리 출력
print(len(contour2), hierarchy)

# 가장 바깥 컨투어만 그리기(녹색)
cv2.drawContours(img, contour, -1, (0,255,0), 3)

# 모든 컨투어 그리기
for idx, cont in enumerate(contour2):
    # 랜덤한 컬러 추출
    color = [int(i) for i in np.random.random_integers(0,255,3)]
    # 컨투어 인덱스 마다 랜덤한 컬러로 그리기
    cv2.drawContours(img2, contour2, idx, color, 3)
    # 컨투어 첫 좌표에 인덱스 숫자 표시
    cv2.putText(img2, str(idx), tuple(cont[0][0]), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255))

cv2.imshow("RETR_EXTERNAL", img)
cv2.imshow("RETR_TREE", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()