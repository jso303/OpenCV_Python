# 가우시안 이미지 피라미드
# 영상의 크기를 단계적으로 축소 또는 확대해 피라미드처럼 쌓아 놓는 것

import cv2

img = cv2.imread("./img/girl.jpg")

# 가우시안 이미지 피라미드 축소
smaller = cv2.pyrDown(img)  # img x 1/4

# 가우시안 이미지 피라미드 확대
bigger = cv2.pyrUp(img)     # img x 4

cv2.imshow("img", img)
cv2.imshow("pyrDown", smaller)
cv2.imshow("pyrUp", bigger)
cv2.waitKey(0)
cv2.destroyAllWindows()