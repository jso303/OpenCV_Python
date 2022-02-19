# OpenCV 함수로 블러링 적용하기
# cv2.blur(입력영상, 커널의 크기)
# cv2.boxFilter(입력영상, 출력영상의 dtype, 커널크기로 정규화)

import cv2
import numpy as np

file_name = "./img/taekwonv1.jpg"
img = cv2.imread(file_name)

blur1 = cv2.blur(img, (10,10))
blur2 = cv2.boxFilter(img, -1, (10,10))

# 영상들 옆으로 이어붙이기
merged = np.hstack((img, blur1, blur2))
cv2.imshow("blur", merged)
cv2.waitKey(0)
cv2.destroyAllWindows()