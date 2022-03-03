# 거리 변환으로 전신 스켈레톤 찾기
# 물체의 영역을 정확히 파악하기 위해 사용
# 주변 경계로 부터 가장 먼 곳을 찾는 방식

import cv2
import numpy as np

img = cv2.imread("./img/full_body.jpg", cv2.IMREAD_GRAYSCALE)
_, biimg = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)

# 거리 변환으로 대략적 뼈대 찾기
# cv2.distanceTransform(입력 영상, 거리 계산 방식, 거리 변환 커널 크기)
dst = cv2.distanceTransform(biimg, cv2.DIST_L2, 5)
dst = (dst/(dst.max()-dst.min())*255).astype(np.uint8)

# 거리 값에 스레시홀드로 완전한 뼈대 찾기

# 적응형 이진화 함수
# cv2.adaptiveThreshold(입력 영상, 최대 값, 적응형 이진화 플래그 \
# (GAUSSIAN_C 는 가우시안 가중치로 적용, MEAN_C 는 평균 가중치 적용),\
# 임계값 형식, 블록 크기, 감산 값)
skeleton = cv2.adaptiveThreshold(dst, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
                                cv2.THRESH_BINARY, 7, -3)

merged = np.hstack((img,dst,skeleton))
cv2.imshow("distanceTrans", merged)
cv2.waitKey()
cv2.destroyAllWindows()