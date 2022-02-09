import cv2
import numpy as np

img = cv2.imread("./img/fish.jpg")
height, width = img.shape[:2]

# 0.5배 축소 변환행렬
m_small = np.float32([[0.5, 0,0], [0,0.5,0]])

# 2배 확대 변환행렬
m_big = np.float32([[2,0,0], [0,2,0]])

# 보간법 적용 없이 확대/축소
dst1 = cv2.warpAffine(img, m_small, (int(height*0.5), int(width*0.5)))
dst2 = cv2.warpAffine(img, m_big, (int(height*2), int(width*2)))

# 보간법 적용한 확대/축소
# 보간법 = 나와있지 않은 부분을 예측하여 값을 추정하여 넣는것
# 보간법을 사용하면 좀 더 깔끔한 이미지 출력 가능
dst3 = cv2.warpAffine(img, m_small, (int(height*0.5), int(width*0.5)),\
                      None, cv2.INTER_AREA)
dst4 = cv2.warpAffine(img, m_big, (int(height*2), int(width*2)),\
                      None, cv2.INTER_CUBIC)

cv2.imshow("original", img)
cv2.imshow("small", dst1)
cv2.imshow("big", dst2)
cv2.imshow("small INTER_AREA", dst3)
cv2.imshow("big INTER_CUBIC", dst4)
cv2.waitKey(0)
cv2.destroyAllWindows()