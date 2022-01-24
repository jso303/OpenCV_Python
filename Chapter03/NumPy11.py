# 검색 : 배열 안에서 데이터 탐색

# np.where(조건식, 맞을 경우의 표시, 틀릴 경우의 표시)

import numpy as np

a = np.arange(0,5)  # [0 1 2 3 4]

print(np.where(a>2, 1, 0))  # True = 1 / False = 0 # [0 0 0 1 1]
print(np.where(a>2, 'T', 'F'))  # True = 'T' / False = 'F'  # ['F' 'F' 'F' 'T' 'T']
print(np.where(a>2, a, 99))     # True = a / False = 99     # [99 99 99 3 4]

b = np.arange(12).reshape(3,4)
print(b)
print(np.where(b>6, 'T','F'))   # True = 'T' / False = 'F'