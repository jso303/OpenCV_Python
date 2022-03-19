# mnist 모듈을 사용하여 MNIST 손글씨 숫자 분류하기

from logging import critical
import cv2
import numpy as np
import matplotlib.pyplot as plt
import mnist    # 만들어둔 모듈 import

# 공통 모듈로부터 MINST 전체 이미지 데이터 읽기
data, _ = mnist.getData()

# 중지 요건
criteria = (cv2.TermCriteria_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
# 평균 클러스터링 적용, 10개 그룹으로 묶음
ret, label, center = cv2.kmeans(data, 10, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
# 중앙점 이미지 출력
for i in range(10):
    # 각 중앙점 값으로 이미지 생성
    cent_img = center[i].reshape(20,20).astype(np.uint8)
    plt.subplot(2,5, i+1)
    plt.imshow(cent_img, "gray")
    plt.xticks([])
    plt.yticks([])
plt.show()
