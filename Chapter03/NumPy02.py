# numpy 초기화

import numpy as np

print(np.zeros(5))                      # 0으로 초기화된 배열 생성
print(np.ones((3,5)))                   # 1로 초기화된 배열 생성
print(np.full((2,3),5))                 # 설정한 값(5)로 초기화된 배열 생성
print(np.arange(0,10,2))                # 0~9까지 2의 간격을 지닌 원소를 지닌 배열 생성
print(np.linspace(0,100,5, dtype=int))  # 0~100 사이 값을 5의 균등한 값으로 구성한 배열 생성

# numpy 난수
print(np.random.random((3,3)))          # (3,3) 배열에 0~1 사이의 난수를 집어넣은 배열
print(np.random.randint(0,10, (3,3)))   # (3,3) 배열에 0~9 사이의 정수 난수를 집어넣은 배열
print(np.random.normal(0,1,(3,3)))      # (3,3) 배열에 평균 0, 표준편차 1을 가진 정규 분포 값을 넣은 배열
print(np.random.randn(3,3))             # (3,3) 배열에 평균 0, 분산 1을 가진 표준정규 분포 값을 넣은 배열
