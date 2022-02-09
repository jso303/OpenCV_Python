import cv2
import numpy as np

img = cv2.imread("./img/fish.jpg")
height, width = img.shape[:2]

# 보간법 알고리즘 선택 플래그인 interpolation 의 자동완성으로 
# Interpolation이 나오는데 그렇게 하면 오류 발생함! 주의

# cv2.resize(입력 영상, 출력 영상 크기(width, height), 배율, 보간법 알고리즘 선택)

# 0.5 크기로 축소
# dst1 = cv2.resize(img, (int(width*0.5), int(height*0.5)), None, 0, 0, cv2.INTER_AREA)
dst1 = cv2.resize(img, (int(width*0.5), int(height*0.5)), interpolation=cv2.INTER_AREA)

# 2배로 확대
dst2 = cv2.resize(img, None, None, 2, 2, cv2.INTER_CUBIC)

cv2.imshow("original", img)
cv2.imshow("small", dst1)
cv2.imshow("big", dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()