# 형태 변환 (차원 변경) reshape

import numpy as np

# reshape 는 (행,열)크기로 변환
# -1은 크기에 맞게 자동으로 지정한다.
arr = np.arange(8)
print(arr)
print("\n")

arr = arr.reshape(-1,4)
print(arr)
print("\n")

# .T : 전치배열, 행과 열을 바꾼다 
print(arr.T)


# 브로드캐스팅 연산 : 배열에 대한 연산, 행렬의 구조를 동일하게 맞춰준다.
# 행렬 복제를 하여 같은 행렬 구조를 가지게 만든 뒤 계산해 준다.

# ex) 1x10 행렬에 대하여 +1 하는 연산 => 값이 모두 1을 가진 1x10 행렬을 만든 뒤 연산을 진행함

a = np.arange(10)
print(a)
a = a+1 # 배열 전체에 +1 연산
print(a)
a = a*2 # 배열 전체에 *2 연산
print(a)
print("\n")

# ex2) True/False 연산도 가능
test = np.arange(0,5)   # [0,1,2,3,4]
TF_test = test > 2      # 2 초과일 경우 True, 이하일 경우 False
print(TF_test)          # [False, False, False, True, True]

# 배열끼리 연산도 가능하다
# 단, 배열 연산의 경우 두 배열의 shape가 동일하거나
# 둘 중 하나가 1차원이면서 1차원 배열의 축의 길이가 같아야 한다.

b = np.arange(10,60,10) # [10,20,30,40,50]
c = np.arange(1,6)      # [1,2,3,4,5]

print(b)
print(c)
print("\n")

d = b+c
print(d)    # [11,22,33,44,55]
e = b*c
print(e)    # [10,40,90,160,250]
f = b/c
print(f)    # [10,10,10,10,10]