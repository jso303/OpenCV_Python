# mask와 누적 할당 연산

import cv2
import numpy as np

# 연산에 사용할 배열 생성
a = np.array([[1,2]], dtype=np.uint8)
b = np.array([[10,20]], dtype=np.uint8)

# 두 번째 요소가 0인 마스크 배열 생성
mask = np.array([[1,0]], dtype=np.uint8)

# 누적 할당과의 비교 연산
c1 = cv2.add(a,b,None,mask)     # 첫번째와 두번째 파라미터의 합을 세번째 파라미터에 저장 
print(c1)                       # a+b 인 [11,22] 가 나와야하지만 mask의 두번째 요소가 0이므로 
                                # 2+20 연산은 수행되지 않아 0이 된다.
                                
c2 = cv2.add(a,b,b,mask)        # 하지만 누적 할당을 적용한 c2의 경우
print(c2)                       # [11,20] 으로 기본 값을 b로 두기 때문에 계산을 수행하지 않는
                                # 두번째 인자 값은 b의 기본 값인 20으로 저장됨.

print(b)    # 단, b 값에 덮어씌우는 형식이 되므로 b값은 [10,20]이 아닌 [11,20]이 저장되어 있다.
            # 만약 b 값을 연산 전 상태로 유지하고 싶다면 c2 = cv2.add(a,b,b.copy(),mask) 형태로 사용하면 된다.
