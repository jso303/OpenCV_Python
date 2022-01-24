# 팬시 인덱싱 : 배열 인덱스에 다른 배열을 전달하여 원하는 요소를 추출(선택)하는 방법

import numpy as np

X = np.arange(12).reshape(3,4)
print(X)

row = np.array([0,1,2])
col = np.array([1,2,3])

print(X[row])   # 0,1,2 행 추출
print(X[:,col])   # 1,2,3 열 추출

print(X[row,col])   # (0,1) (1,2) (2,3) 행열 추출 = 1,6,11
print(X[row.reshape(-1,1),col]) # reshape를 이용해 구조를 변환해도 동일한 결과를 냄

