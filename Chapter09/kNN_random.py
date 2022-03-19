# K-NN 난수 분류
# 최근접 이웃 알고리즘
# 입력 데이터를 최근접 이웃 데이터로 분류
# 가중치 부여할 수 있음

import cv2
import numpy as np
import matplotlib.pyplot as plt

# 0~99 사이의 랜덤한 수 50(25 x 2)개 데이터 생성
trainData = np.random.randint(0,100,(25,2)).astype(np.float32)
# 0~1 사이의 랜덤한 수 25(25 x 1)개 레이블 생성
labels = np.random.randint(0,2,(25,1))
# 레이블 값 0과 같은 자리는 red, 1과 같은 자리는 blue로 분류해서 표시
red = trainData[labels.ravel()==0]
blue = trainData[labels.ravel()==1]
plt.scatter(red[:,0], red[:,1], 80, "r", "^")   # 빨간색 삼각형
plt.scatter(blue[:,0], blue[:,1], 80, "b", "s") # 파란색 사각형

# 0~99 사이의 랜덤 수 신규 데이터 생성
newcomer = np.random.randint(0,100, (1,2)).astype(np.float32)
plt.scatter(newcomer[:,0], newcomer[:,1], 80, "g", "o")     # 초록색 원

# KNearest 알고리즘 객체 생성
knn = cv2.ml.KNearest_create()
knn.train(trainData, cv2.ml.ROW_SAMPLE, labels)

# 예측 결과 데이터, 입력 데이터에 대한 예측 결과, K 범위 내에 있는 이웃 데이터\
# , 이웃 데이터와의 거리 = knn.findNearest(입력 데이터, 이웃 범위 지정을 위한 K)
# 범위 3 내의 이웃 데이터 숫자가 많은 쪽의 데이터로 분류함
ret, results, neighbors, dist = knn.findNearest(newcomer, 3)

print("ret:%s, result:%s, negibours:%s, distance:%s" %(ret,results,neighbors,dist))

plt.annotate("red" if ret==0.0 else "blue", xy=newcomer[0], xytext=(newcomer[0]+1))
plt.show()