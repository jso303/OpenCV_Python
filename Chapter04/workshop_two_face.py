# 반해골 괴물 얼굴 합성

# 사용파일 : 얼굴 : img/man_face.jpg, 해골 : img/skull.jpg

import cv2
import numpy as np

# 알파 값이 적용될 범위
alpha_width_rate = 40

img_man = cv2.imread("./img/man_face.jpg")
img_skull = cv2.imread("./img/skull.jpg")

# 빈 이미지 생성
img_result = np.zeros_like(img_man)

# 이미지의 중간 위치 계산
height, width = img_man.shape[:2]
middle = width//2
alpha_width = width * alpha_width_rate // 100

# 점점 바뀌는 이미지 생성을 위한 좌표값 계산
start = middle - alpha_width//2
step = 100/alpha_width

# img3를 왼쪽은 img1, 오른쪽은 img2로 채움
img_result[:,:middle,:] = img_man[:,:middle,:].copy()
img_result[:,middle:,:] = img_skull[:,middle:,:].copy()

# 알파 값을 중앙에 가까워 질때 증가시키며 알파 블렌딩 적용
for i in range(alpha_width+1):
    alpha = (100 - step * i) / 100
    beta = 1 - alpha
    img_result[:,start+i] = img_man[:,start+i] * alpha + img_skull[:,start+i] * beta
    print(i, alpha, beta)

cv2.imshow("man", img_man)
cv2.imshow("skull", img_skull)
cv2.imshow("blending", img_result)
cv2.waitKey()
cv2.destroyAllWindows()