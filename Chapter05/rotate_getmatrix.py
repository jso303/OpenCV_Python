# 회전을 위한 변환행렬 생성 없이 간단하게 회전시키는 OpenCV 함수
# cv2.getRotationMatrix2D(회전 축 중심 좌표(x,y), 회전각도, 확대/축소 배율)

import cv2

img = cv2.imread("./img/fish.jpg")
rows,cols = img.shape[0:2]

# 중앙 축, 45도, 0.5배
m45 = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 0.5)
# 중앙 축, 90도, 1.5배
m90 = cv2.getRotationMatrix2D((cols/2, rows/2), 90, 1.5)

img45 = cv2.warpAffine(img, m45, (cols, rows))
img90 = cv2.warpAffine(img, m90, (cols, rows))

cv2.imshow("origin", img)
cv2.imshow("45", img45)
cv2.imshow("90", img90)
cv2.waitKey(0)
cv2.destroyAllWindows()