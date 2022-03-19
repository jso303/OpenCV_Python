# 실제로 쓴 숫자 인식하기
# kNN_mnist에서 정확도가 가장 높았던 k=1 로 인식

import cv2
import numpy as np
from sklearn import neighbors
import mnist

# 훈련 데이터 가져오기
train, train_labels = mnist.getData()
# knn 객체 생성 및 학습
knn = cv2.ml.KNearest_create()
knn.train(train, cv2.ml.ROW_SAMPLE, train_labels)

# 인식시킬 손글씨 이미지 읽기
# 4027이 교재 예제이지만 직접 쓴 글씨에 정상 작동하는지 확인을 위한 519.png로도 실습
# image = cv2.imread("./img/519.png")     
image = cv2.imread("./img/4027.png")     
cv2.imshow("image", image)
cv2.waitKey(0)

# 그레이 스케일로 변환과 스레시홀드
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5,5), 0)
_, gray = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
# 최외곽 컨투어만 찾기
contours, _ = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 모든 컨투어 순회
for c in contours:
    # 컨투어를 감싸는 외접 사각형으로 숫자 영역 좌표 구하기
    (x,y,w,h) = cv2.boundingRect(c)
    # 외접 사각형의 크기가 너무 작은것은 제외
    if w >= 5 and h >= 25:
        # 숫자 영역만 roi로 확보하고 사각형 그리기
        roi = gray[y:y+h, x:x+w]
        cv2.rectangle(image, (x,y), (x+w, y+h), (0,255,0), 1)
        data = mnist.digit2data(roi)
        ret, result, neighbors, dist = knn.findNearest(data, k=1)
        cv2.putText(image, "%d"%ret, (x,y+155), cv2.FONT_HERSHEY_DUPLEX, 2, (255,0,0),2)
        cv2.imshow("image", image)
        cv2.waitKey(0)
cv2.destroyAllWindows()