# 슬라이싱

# ':' 으로 되어 있는 연산자 사용

import numpy as np
arr = np.arange(10)

print(arr)

# [start:end:step]  #[시작:끝:간격]
# start는 생략 시 0, end는 생략 시 끝까지, step는 생략 시 1을 사용한다.
print(arr[0:5:1])
print(arr[:5:1])
print(arr[:5:])
print(arr[:5])

print(arr[2:9:2])
print(arr[2::2])

# -1은 역순으로 셈한다.
print(arr[::-1])
print(arr[-1:-11:-1])
print(arr[5::-1])
