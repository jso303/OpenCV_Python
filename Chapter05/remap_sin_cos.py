# 삼각함수를 이용한 비선형 리매핑

import cv2
import numpy as np

l = 20
amp = 15

img = cv2.imread("./img/taekwonv1.jpg")
rows, cols = img.shape[:2]

mapy, mapx = np.indices((rows, cols), dtype=np.float32)     # 초기 매핑 배열

# sin, cos 함수를 이용한 변형 매핑 연산
sinx = mapx + amp * np.sin(mapy/l)
cosy = mapy + amp * np.cos(mapx/l)

img_sinx = cv2.remap(img, sinx, mapy, cv2.INTER_LINEAR)     # x 축만 sin 곡선 적용
img_cosy = cv2.remap(img, mapx, cosy, cv2.INTER_LINEAR)     # y 축만 cos 곡선 적용

img_both = cv2.remap(img, sinx, cosy, cv2.INTER_LINEAR, \
                     None, cv2.BORDER_REPLICATE)            # x축 sin, y축 cos 적용, 빈 외각 영역 보정

cv2.imshow("origin", img)
cv2.imshow("sin x", img_sinx)
cv2.imshow("cos y", img_cosy)
cv2.imshow("sin cos", img_both)

cv2.waitKey()
cv2.destroyAllWindows()