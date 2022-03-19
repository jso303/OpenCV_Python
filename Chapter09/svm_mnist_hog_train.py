# MNIST 손글씨 HOG-SVM 학습
# HOG는 보행자 검출을 목적으로 만들어진 특징 디스크립터
# 지역적인 특징보다는 전체적인 특징을 잡아 대상 객체의 상태나 자세가 약간 다르더라도 인식함
# 해당 예제는 보행자 검출을 하기 전 손글씨 검출로 사용 원리를 연습한다.

# 테스트 결과 값
# SVM training started...train data: (50, 90, 324)      # 학습 이미지 HOG 값
# SVM training complete. 8.79 Min                       # 학습 실행 시간
# Accuracy: 98.80%                                      # 정확도

import cv2
import numpy as np
import mnist
import time

affine_flags = cv2.WARP_INVERSE_MAP|cv2.INTER_LINEAR

# 기울어진 숫자를 바로 세우기 위한 함수
# 숫자 하나의 모멘트를 계산해 중심점을 기준으로 기울어진 숫자를 바로 세움   
def deskew(img):
    m = cv2.moments(img)
    if abs(m["mu02"]) < 1e-2:
        return img.copy()
    skew = m["mu11"]/m["mu02"]
    # 변환행렬 설정
    M = np.float32([[1, skew, -0.5*20*skew], [0,1,0]])
    # # cv2.warpAffine(원본영상, 변환행렬, 결과이미지크기, 결과이미지, 보간법 알고리즘 선택)
    img = cv2.warpAffine(img,M,(20,20),flags=affine_flags)
    return img

# HOGDescriptor을 위한 파라미터 설정 및 생성
winSize = (20,20)
blockSize = (10,10)
blockStride = (5,5)
cellSize = (5,5)
nbins = 9
hogDesc = cv2.HOGDescriptor(winSize,blockSize,blockStride,cellSize,nbins)

if __name__ =="__main__":
    # MNIST 이미지에서 학습용 이미지와 테스트 이미지 가져오기
    train_data, train_label = mnist.getTrain(reshape=False)
    test_data, test_label = mnist.getTest(reshape=False)
    
    # 학습 이미지 글씨 바로 세우기
    deskewed = [list(map(deskew,row)) for row in train_data]
    
    # 학습 이미지 HOG 계산
    hogdata = [list(map(hogDesc.compute,row)) for row in deskewed]
    train_data = np.float32(hogdata)
    print("SVM training started...train data:", train_data.shape)
    
    # 학습용 HOG 데이터 재배열
    train_data = train_data.reshape(-1,train_data.shape[2])
    
    # SVM 알고리즘 객체 생성 및 훈련
    svm = cv2.ml.SVM_create()
    startT = time.time()
    svm.trainAuto(train_data, cv2.ml.ROW_SAMPLE, train_label)
    endT = time.time() - startT
    print("SVM training complete. %.2f Min" %(endT/60))
    
    # 훈련된 결과 모델 저장
    svm.save("svm_mnist.xml")
    
    # 테스트 이미지 글씨 바로 세우기 및 HOG 계산
    deskewed = [list(map(deskew,row)) for row in test_data]
    hogdata = [list(map(hogDesc.compute,row)) for row in deskewed]
    test_data = np.float32(hogdata)
    
    # 테스트용 HOG 데이터 재배열
    test_data = test_data.reshape(-1, test_data.shape[2])
    
    # 테스트 결과 예측 
    ret, result = svm.predict(test_data)
    correct = (result==test_label).sum()
    
    # 예측 결과와 테스트 레이블이 맞은 개수 합산 및 정확도 출력
    print("Accuracy: %.2f%%" %(correct*100.0/result.size))