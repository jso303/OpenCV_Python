import cv2
import numpy as np
import matplotlib.pylab as plt

img1 = np.zeros((200,400), dtype=np.uint8)  # 200x400의 0비트(검은색) 이미지 생성
img2 = np.zeros((200,400), dtype=np.uint8)

# [세로, 가로]
img1[:,:200] = 255      # 왼쪽은 검은색(0), 오른쪽은 흰색(255)
img2[100:200, :] = 255  # 위쪽은 검은색(0), 아래쪽은 흰색(255)

# 비트 연산
bitAnd = cv2.bitwise_and(img1,img2)     # and 연산, 둘 다 0인 부분만 0으로 채움, 나머지 255
bitOr = cv2.bitwise_or(img1,img2)       # or 연산, 둘 중 하나만 0이여도 0으로 채움, 나머지 255
bitXor = cv2.bitwise_xor(img1,img2)     # xor 연산, 둘의 값이 다르면 0으로 채움, 나머지 255
bitNot = cv2.bitwise_not(img1)          # not(img1) 연산, 원래 이미지와 반대값

imgs = {"img1":img1, "img2":img2, "and":bitAnd, "or":bitOr, "xor":bitXor, "not(img1)":bitNot}

for i, (title, img) in enumerate(imgs.items()):
    plt.subplot(3,2,i+1)
    plt.title(title)
    plt.imshow(img, "gray")
    plt.xticks([])
    plt.yticks([])
    
plt.show()