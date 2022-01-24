# NumPy 배열의 기본 속성

# ndim      : 차원(축)의 수
# shape     : 각 차원의 크기(튜플)
# size      : 전체 요소의 개수, 각 차원 항목의 곱
# dtype     : 요소의 데이터 타입
# itemsize  : 각 요소의 바이트 크기

# ex)
import cv2
img = cv2.imread("./img/Ch02_img/blank_500.jpg")
print(type(img))        # <class 'numpy.ndarray'> 출력됨

print(img.ndim)         # 3                 # 3차원
print(img.shape)        # (500, 500, 3)     #(500 x 500 x 3) 배열
print(img.size)         # 750000            # 배열곱
print(img.dtype)        # uint8             # 부호없는 8비트
print(img.itemsize)     # 1                 # 각 요소의 크기가 1바이트