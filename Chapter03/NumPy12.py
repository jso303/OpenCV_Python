# 기초 통계 함수

# sum   : 합
# mean  : 평균
# amin  : 최소 값
# min   : 최소 값
# amax  : 최대 값
# max   : 최대 값


import numpy as np

a = np.arange(12).reshape(3,4)
print(a)

print(np.sum(a))    # 배열의 합
print(np.mean(a))   # 배열의 평균
print(np.amin(a))   # 배열의 최소 값
print(np.min(a))    # 배열의 최소 값
print(np.amax(a))   # 배열의 최대 값
print(np.max(a))    # 배열의 최대 값

