# 단일 원소에 접근하는 기법 : 인덱싱

import numpy as np

np.random.seed(0)


arr1 = np.random.randint(0,10,size=6)
print(arr1)                             # [5 0 3 3 7 9]

print(arr1[0])                          # 5
print(arr1[5])                          # 9 

print(arr1[-6], arr1[-1])               # 5 9       # -의 경우 뒤에서 부터 셈한다.


arr2 = np.random.randint(0,10, size=(2,3))
print(arr2)                             # [[3 5 2] 
                                        #  [4 7 6]]
print(arr2[0])                          # [3 5 2]
print(arr2[0,0])                        # 3 
print(arr2[1,2])                        # 6
print(arr2[0,1])                        # 5


# 인덱싱을 이용해 새로운 값 지정 가능

arr2[0,1] = 9                           # arr2의 0,1 위치의 값을 9로 변경 (기존 5)
print(arr2[0,1])                        # 9
