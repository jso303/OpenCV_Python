# 라플라시안 피라미드로 영상 복원

# 가우시안 피라미드로 영상 확대 후 축소 시 원본 영상과 오차가 생김
# 원본과 cv2.pyrUP 함수를 적용한 영상의 차이를 단계별로 모아두는 것을 라플라시안 피라미드라 함
# 라플라시안 피라미드가 경계를 검출함
# 흐릿한 영상에 경계를 더해주면 선명한 영상으로 복원 가능

# 영상 복원 뿐만 아니라 경계 검출에도 사용 가능하다

import cv2
import numpy as np

img = cv2.imread("./img/taekwonv1.jpg")

# 원본 영상을 가우시안 피라미드로 축소
smaller = cv2.pyrDown(img)
# 축소한 영상을 가우시안 피라미드로 확대
bigger = cv2.pyrUp(smaller)

# 원본에서 축소 후 확대한 영상 빼기
laplacian = cv2.subtract(img, bigger)
# 확대한 영상에 라플라시안 영상을 더해서 복원
restored = bigger + laplacian

# 원본 영상 / 라플라시안 / 확대 영상 / 복원 영상
merged = np.hstack((img, laplacian, bigger, restored))
cv2.imshow("Laplacian Pyramid", merged)
cv2.waitKey(0)
cv2.destroyAllWindows()