import cv2
import numpy as np

img = cv2.imread("./img/sunset.jpg")

x=277; y=72; w=60; h=60        # roi 좌표
roi = img[y:y+h, x:x+w]         # roi 관심영역 지정

print(roi.shape)                # roi shape, (60,60,3)
cv2.rectangle(roi, (0,0), (h-1, w-1), (0,255,0))    # roi에 사각형을 그려 표시하기
cv2.imshow("img", img)                              # (선을 그리기 위해 1픽셀을 뺌)

cv2.waitKey(0)
cv2.destroyAllWindows()