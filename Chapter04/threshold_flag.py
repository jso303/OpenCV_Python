import cv2
import numpy as np
import matplotlib.pylab as plt

img = cv2.imread("./img/gray_gradient.jpg", cv2.IMREAD_GRAYSCALE)


# (처리할 이미지, 경계, value, 스레시홀드 적용 방법)
# INV 는 반대라 생각하면 됨

# # 경계 값을 넘으면 value 값, 못 넘으면 0
_, t_bin = cv2.threshold(img, 127,255, cv2.THRESH_BINARY)
# 경계 값을 못 넘으면 value 값, 넘으면 0 (bin의 반대)  
_, t_bininv = cv2.threshold(img, 127,255, cv2.THRESH_BINARY_INV)

# 경계 값을 넘으면 value 값, 못 넘으면 원래 값 유지
_, t_truc = cv2.threshold(img, 127,255, cv2.THRESH_TRUNC)

# 경계 값을 넘으면 원래 값 유지, 못 넘으면 value 값
_, t_2zr = cv2.threshold(img, 127,255, cv2.THRESH_TOZERO)
# 경계 값을 못 넘으면 원래 값 유지, 넘으면 value 값
_, t_2zrinv = cv2.threshold(img, 127,255, cv2.THRESH_TOZERO_INV)

imgs = {"origin":img, "BINARY":t_bin, "BINARY_INV":t_bininv,\
    "TRUNIC":t_truc, "TOZERO":t_2zr, "TOZERO_INV":t_2zrinv}
for i, (key, value) in enumerate(imgs.items()):
    plt.subplot(2,3,i+1)    # 2행 3열에서 순서에 맞게 배치
    plt.title(key)
    plt.imshow(value, cmap="gray")
    plt.xticks([])
    plt.yticks([])
    
plt.show()
