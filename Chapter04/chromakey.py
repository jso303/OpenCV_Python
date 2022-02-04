import cv2
import numpy as np
import matplotlib.pylab as plt

img1 = cv2.imread("./img/man_chromakey.jpg")
img2 = cv2.imread("./img/street.jpg")

# roi 선택을 위한 좌표 계산 (가운데 위치 시키기 위한)
height1, width1 = img1.shape[:2]
height2, width2 = img2.shape[:2]
x = (width2 - width1)//2
y = height2 - height1
w = x + width1
h = y + height1

# 크로마 키가 될만한 지역을 예시 크로마 키로 지정(img1 에서의 왼쪽 위 10 X 10 픽셀)
chromakey = img1[:10, :10, :]
# 크로마 키 영역의 H(색상) 값에서 offset 만큼 여유를 두고 범위 지정
# offset 이 작으면 크로마키가 남을 것이며 크면 전경의 일부도 사라짐
# 여러 차례 시도 후 적절한 offset으로 지정
offset = 20

# 크로마 키 영역과 영상 전체를 HSV로 변경
hsv_chroma = cv2.cvtColor(chromakey, cv2.COLOR_BGR2HSV)
hsv_img = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)

# 크로마 키 영역(녹색)을 인지할 범위 지정
chroma_h = hsv_chroma[:,:, 0]
lower = np.array([chroma_h.min()-offset, 100, 100])
upper = np.array([chroma_h.max()+offset, 255, 255])

# 마스크 생성 및 마스킹 후 합성
mask = cv2.inRange(hsv_img, lower, upper)
mask_inv = cv2.bitwise_not(mask)
roi = img2[y:h, x:w]
fg = cv2.bitwise_and(img1, img1, mask=mask_inv)
bg = cv2.bitwise_and(roi, roi, mask=mask)
img2[y:h, x:w] = fg + bg

cv2.imshow("chromakey", img1)
cv2.imshow("added", img2)
cv2.waitKey()
cv2.destroyAllWindows()