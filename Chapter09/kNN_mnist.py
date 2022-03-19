# 손글씨 인식
# 정확도 예측

import cv2
import numpy as np
import mnist

# 훈련 데이터 가져오기
train, train_labels = mnist.getTrain()
# 테스트 데이터 가져오기
test, test_labels = mnist.getTest()

# knn 객체 생성 및 훈련
knn = cv2.ml.KNearest_create()
knn.train(train, cv2.ml.ROW_SAMPLE, train_labels)

# k 값을 1~10까지 변경하면서 예측
# 가장 정확도가 높은 k 값을 사용하면 됨
# 현재 k가 1일때 정확도가 가장 높으므로 1을 사용하면 됨
for k in range(1,11):
    ret, result, neighbors, distance = knn.findNearest(test, k=k)
    correct = np.sum(result == test_labels)
    accuracy = correct / result.size * 100.0
    print("K:%d, Accuracy:%.2f%%(%d/%d)" % (k, accuracy, correct, result.size))