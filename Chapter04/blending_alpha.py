import cv2
import numpy as np

alpha = 0.5     # 합성에 사용할 알파 값 (50% 합성)

img1 = cv2.imread("./img/wing_wall.jpg")
img2 = cv2.imread("./img/yate.jpg")

# 수식을 NumPy 배열에서 직접 연산하여 알파 블렌딩 적용
blended = img1 * alpha + img2 * (1-alpha)
blended = blended.astype(np.uint8)
cv2.imshow("img1 * alpha + img2 * (1-alpha)", blended)

# addWeighted() 함수로 알파 블렌딩 적용
dst = cv2.addWeighted(img1, alpha, img2, (1-alpha), 0)
cv2.imshow("cv2.addWeighted", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()