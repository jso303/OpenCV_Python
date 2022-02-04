import cv2
import numpy as np

a = np.uint8([[200,50]])
b = np.uint8([[100,100]])

# NumPy 배열 직접 연산
# 마이너스, 255 초과의 경우 마이너스 분, 초과분 만큼 255에서 빼고 0에서 남은 분량 시작
add1 = a + b       # [200+100, 50+100]   # [300, 150] 이 아닌 [44, 150] 이 나옴. 255 초과하는 44 라는 뜻 
sub1 = a - b       # [200-100, 50-100]   # [100, -50] 이 아닌 [100,206] 이 나옴, 256 - 60으로 계산
mult1 = a * 2
div1 = a / 3

# OpenCV API를 이용한 연산
# 최대값 255, 최소값 0
# 소수점은 반올림처리
add2 = cv2.add(a,b)     # [200+100, 50+100]   # [300, 150] 이 아닌 [255, 150]이 나옴, 255 초과 시 255로 표기
sub2 = cv2.subtract(a,b)
mult2 = cv2.multiply(a,2)
div2 = cv2.divide(a,3)

print(add1, add2)
print(sub1, sub2)
print(mult1, mult2)
print(div1, div2)

