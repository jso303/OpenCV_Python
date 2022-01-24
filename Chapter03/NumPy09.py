# 부울 배열

import numpy as np

np.random.seed(0)

X = np.random.randint(1,10, size=(3,4))
print(X)

print( (X>5) & (X<8) )  # (X가 5 초과 : True) & (X가 8 미만 : True)
                        # 6,7 값 True
                        
print(np.sum((X>5)&(X<8)))  # 5초과 & 8미만 = True 값 갯수 합   # & : 둘 다 만족

print(((X>5)|(X<8)))    # 모든 값이 True 범위가 됨
print(np.sum((X>5)|(X<8)))  # 5초과 | 8미만 = True 값 갯수 합   # | : 둘 중 하나 만족

print(((X>5)&(X<8)))  # 5초과 & 8미만 = True   # & : 둘 다 만족
print(np.sum((X>5)&(X<8), axis=0))  # 축 별 True 갯수   (세로 합)
print(np.sum((X>5)&(X<8), axis=1))  # 축 별 True 갯수   (가로 합)

