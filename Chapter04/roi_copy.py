import cv2
import numpy as np

img = cv2.imread("./img/sunset.jpg")

x=277; y=72; w=60; h=60        # roi 좌표
roi = img[y:y+h, x:x+w]        # roi 관심영역 지정
img2 = roi.copy()              # roi 배열 복제 

img[y:y+h, x+w:x+w+w] = roi                          # 새로운 좌표에 roi 추가, 태양 옆에 두번째 태양 만들기
cv2.rectangle(img, (x,y), (x+w+w, y+h), (0,255,0))   # 2번째 태양 영역 사각형 표시

cv2.imshow("img", img)  # 태양이 두개 떠 있는 사진
cv2.imshow("roi", img2) # 복제된 태양

cv2.waitKey(0)
cv2.destroyAllWindows()