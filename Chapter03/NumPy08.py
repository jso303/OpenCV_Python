# 축 기준 연산

import numpy as np

np.random.seed(0)

arr = np.random.randint(1,10,(3,4)) # 1~9 사이 값을 랜덤으로 넣은 (3,4) 행렬 구성
print(arr)

print(np.sum(arr))      # 행렬에 담긴 모든 원소의 합 = 65
print(arr.sum())        # 행렬에 담긴 모든 원소의 합 = 65

# axis 생략 시 0으로 적용됨
print(np.sum(arr, axis=0))  # 0번(세로)축 기준 합 = [19 13 17 16]
print(arr.sum(axis=0))      

print(np.sum(arr, axis=1))  # 1번(가로)축 기준 합 = [15 21 29]
print(arr.sum(axis=1))

print(np.min(arr, axis=0)) # 0번 축 기준 제일 작은 값 연산
print(np.max(arr, axis=1)) # 1번 축 기준 제일 큰 값 연산