# 평균 필터를 생성하여 사진에 블러 적용(흐려짐 효과)

import cv2
import numpy as np

img = cv2.imread("./img/girl.jpg")

# 5x5 평균 필터 커널 생성
kernel = np.array([[0.04, 0.04, 0.04, 0.04, 0.04],
                   [0.04, 0.04, 0.04, 0.04, 0.04],
                   [0.04, 0.04, 0.04, 0.04, 0.04],
                   [0.04, 0.04, 0.04, 0.04, 0.04],
                   [0.04, 0.04, 0.04, 0.04, 0.04]])

# 5x5 평균 필터 커널 생성
kernel = np.ones((5,5))/5**2

# 필터 적용
# cv2.filter2D(입력 영상, 출력 영상의 dtype, 컨볼루션 커널)
# 출력 영상 dtype : -1 == 입력 영상과 동일
blured = cv2.filter2D(img, -1, kernel)

cv2.imshow("origin", img)
cv2.imshow("avrg blur", blured)
cv2.waitKey()
cv2.destroyAllWindows()