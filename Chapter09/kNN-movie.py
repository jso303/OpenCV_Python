# k-NN 영화 장르 분류
# 발차기 장면과 키스 장면의 횟수로 액션 영화인지 로맨스 영화인지 장르 분류

import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn import neighbors

# 0~99 사이의 랜덤 값 25 x 2
trainData = np.random.randint(0,100,(25,2)).astype(np.float32)
responses = (trainData[:,0] > trainData[:,1]).astype(np.float32)
# responses 값 0 : 액션 영화, 1: 로맨스 영화
action = trainData[responses==0]
romantic = trainData[responses==1]

# action은 파란색 삼각형, romantic은 빨간색 동그라미로 표시
plt.scatter(action[:,0], action[:,1], 80, "b", "^", label="action")
plt.scatter(romantic[:,0], romantic[:,1], 80, "r", "o", label="romantic")
# 새로운 데이터 생성, 0~99 랜덤 수 1 x 2, 초록색 사각형으로 표시
newcomer = np.random.randint(0,100,(1,2)).astype(np.float32)
plt.scatter(newcomer[:,0], newcomer[:,1], 200, "g", "s", label="new")

# Knearest 알고리즘 생성 및 훈련
knn = cv2.ml.KNearest_create()
knn.train(trainData, cv2.ml.ROW_SAMPLE, responses)

ret, results, neighbors, dist = knn.findNearest(newcomer, 3)
print("ret:%s, result:%s, neighbours:%s, dist:%s" %(ret,results,neighbors,dist))

# 새로운 결과에 화살표로 표시
anno_x, anno_y = newcomer.ravel()
label = "action" if results == 0 else "romantic"
plt.annotate(label, xy=(anno_x+1, anno_y+1),\
             xytext=(anno_x+5, anno_y+10), arrowprops={"color":"black"})
plt.xlabel("kiss")
plt.ylabel("kick")
plt.legend(loc="upper right")
plt.show()