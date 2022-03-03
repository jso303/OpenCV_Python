# 도형 알아맞히기 워크숍
# 컨투어를 찾아 근사 값으로 단수화해서 꼭지점의 개수를 센다.

import cv2
import numpy as np

img = cv2.imread("./img/5shapes.jpg")
img2 = img.copy()
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)      
ret, th = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY_INV)

# 컨투어(경계) 찾기
contours, _ = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    # 근사 컨투어로 단순화 (대략적인 경계 모양만 구분)
    approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)
    # 꼭지점의 개수
    vertices = len(approx)
    
    # 중심점 찾기
    mmt = cv2.moments(contour)
    cx, cy = int(mmt["m10"]/mmt["m00"]), int(mmt["m01"]/mmt["m00"])
    
    name = "Unkown"
    if vertices == 3:       # 꼭지점 3개는 삼각형
        name = "Triangle"
        color = (0,255,0)   # 녹색
    elif vertices == 4:     # 꼭지점 4개는 사각형
        x,y,w,h = cv2.boundingRect(contour) 
        if abs(w-h) <=3:    # 폭과 높이의 차이가 3픽셀 이하이면 정사각형
            name = "Square"
            color = (0,125,255) # 주황색
        else:
            name = "Rectangle"  # 이외에는 직사각형
            color = (0,0,255)   # 빨간색
    elif vertices == 10:    # 꼭지점 10개는 별
        name = "Star"
        color = (255,255,0) # 청록색
    elif vertices >= 15:    # 꼭지점 15개 이상은 원
        name = "Circle"
        color = (0,255,255) # 적녹색
        
    # 컨투어 그리기
    cv2.drawContours(img2, [contour], -1, color, -1)
    # 도형 이름 출력(name 출력)
    cv2.putText(img2, name, (cx-50, cy), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (100,100,100), 1)
    
cv2.imshow("Input Shapes", img)
cv2.imshow("Recongnizing Shapes", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()