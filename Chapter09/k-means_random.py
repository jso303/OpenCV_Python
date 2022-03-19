# 랜덤한 수 군집화

import cv2
import numpy as np
import matplotlib.pyplot as plt

# 0~150 사이의 임의의 두 수, 25개
a = np.random.randint(0,150,(25,2))
# 128~255 사이의 임의의 두수, 25개
b = np.random.randint(128,255,(25,2))

data = np.vstack((a,b)).astype(np.float32)

# 반복 중지 요건
criteria = (cv2.TermCriteria_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

# cv2.kmeans(처리 대상 데이터, 원하는 묶음 개수, 결과데이터, 반복 종료 요건,\
#           매번 다른 초기 레이블로 실행할 횟수, 초기 중앙점 선정 방법)
ret, label, center = cv2.kmeans(data,2,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

# label에 따라 결과 분류
red = data[label.ravel()==0]
blue = data[label.ravel()==1]

# plot에 결과 출력 
plt.scatter(red[:,0], red[:,1], c='r')
plt.scatter(blue[:,0],blue[:,1], c='b')

plt.scatter(center[0,0],center[0,1], s=100, c='r', marker='s')
plt.scatter(center[1,0],center[1,1], s=100, c='b', marker='s')
plt.show()