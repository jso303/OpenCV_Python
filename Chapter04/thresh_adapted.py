# 적응형 스레시홀드
# 조명이 일정하지 않거나 배경색이 여러가지 일 경우 기존 스레시홀드 방식으로는 좋은 값을 얻기가 힘듬
# 이미지를 여러 영역으로 나눈 다음 주변 픽셀로만 계산 하여 각 영역별로 경계 값을 구하여 적용시키는 방식

import cv2
import numpy as np
import matplotlib.pylab as plt

blk_size = 9    # 블록 사이즈 (n X n, 현재 9x9 사이즈)
C = 5           # 차감 합수 (계산된 경계 값 결과에서 가감할 상수)

# 기본 이미지 그레이 스케일로 읽기
img = cv2.imread("./img/sudoku.png", cv2.IMREAD_GRAYSCALE)

# 오츠 알고리즘으로 단일 경계 값을 전체에 적용
ret, th1 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
# 적응형 스레시홀드를 이웃 픽셀의 평균으로 적용
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, \
                                    cv2.THRESH_BINARY, blk_size, C)
# 적응형 스레시홀드를 가우시안 분포에 따른 이웃 픽셀의 가중치의 합으로 적용
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
                                    cv2.THRESH_BINARY, blk_size, C)

imgs = {"Original":img, "Global-Otsu:%d"%ret:th1,\
        "Adapted-Mean":th2, "Adated-Gassian":th3}

for i, (key, value) in enumerate(imgs.items()):
    plt.subplot(2,2,i+1)    # 2행2열에 순서대로 배치
    plt.title(key)
    plt.imshow(value,"gray")
    plt.xticks([])
    plt.yticks([])
    
plt.show()