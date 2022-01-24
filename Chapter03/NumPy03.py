# 랜덤 값의 재현성 문제

import numpy as np

np.random.seed(0)       # 코드를 실행 할 때 처음 나온 값을 시드 값으로 저장해둠    
                        # 해당 코드를 다시 실행할 때 같은 값이 나온다.  (단, 다른 코드에서 실행할 시 다른 값이 나옴)

arr1 = np.random.randint(10, size=6)
arr2 = np.random.randint(10, size=(2,3))

print("arr1 :\n %s" %arr1)
print("ndim : %d, shape : %s, size : %s, dtype : %s\n" \
    %(arr1.ndim, arr1.shape, arr1.size, arr1.dtype))

print("arr2 :\n %s" %arr2)
print("ndim : %d, shape : %s, size : %s, dtype : %s\n"\
    %(arr2.ndim, arr2.shape, arr2.size, arr2.dtype))