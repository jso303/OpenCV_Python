# 모멘트를 이용한 중심점, 넓이, 둘레길이

import cv2
import numpy as np

img = cv2.imread("./img/shapes.png")

imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, th = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY_INV)

contours, hierachy = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 각 도형의 컨투어에 대한 루프
for c in contours:
    # 모멘트 계산
    # cv2.moments(모멘트 계산 대상 컨투어 좌표)
    mmt = cv2.moments(c)
    cx = int(mmt["m10"]/mmt["m00"])
    cy = int(mmt["m01"]/mmt["m00"])
    
    # 영역 너비
    a = mmt["m00"]
    
    # 영역 외각선 길이
    # cv2.arcLength(넓이를 계산할 컨투어, 컨투어 방향 플래그
    # (True == 컨투어 방향에 따라 음수 반환, False== 절대 값 반환))
    l = cv2.arcLength(c, True)
    # 중심에 노란색 점 그리기
    cv2.circle(img, (cx,cy), 5, (0,255,255), -1)
    # 중심점 근처에 넓이 그리기
    cv2.putText(img, "A:%.0f"%a, (cx,cy+20), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255))
    # 컨투어 시작점에 길이 그리기
    cv2.putText(img, "L:%.2f"%l, tuple(c[0][0]), cv2.FONT_HERSHEY_PLAIN, 1, (255,0,0))
    
    # 함수로 컨투어 넓이 계산해서 출력
    # cv2.contourArea(둘레 길이를 계산할 컨투어, 닫힌 호인지 여부 플래그)
    print("area:%.2f"%cv2.contourArea(c, False))
    
cv2.imshow("center", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
    