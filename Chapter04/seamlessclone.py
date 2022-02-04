import cv2
import numpy as np
import matplotlib.pylab as plt

img1 = cv2.imread("./img/drawing.jpg")
img2 = cv2.imread("./img/my_hand.jpg")

# 마스크 생성, 합성할 이미지 전체 영역을 255로 세팅
mask = np.full_like(img1, 255)
 
# 합성 대상 좌표 계산(img2의 중앙이 되도록)
height, width = img2.shape[:2]
center = (width//2, height//2)      # 전체 width와 height의 1/2 위치

# seamlessClone(전경, 배경, 마스크, 전경이 위치할 좌표, 합성방식)
# normal의 경우 단순 덮어 쓰기로서 그림의 선명도는 강하지만 손의 색만 바탕으로 사용
# mixed의 경우 손과 그림이 자연스럽게 융화되도록 합성함, 그림의 선명도는 약해짐 
normal = cv2.seamlessClone(img1, img2, mask, center, cv2.NORMAL_CLONE)
mixed = cv2.seamlessClone(img1, img2, mask, center, cv2.MIXED_CLONE)

cv2.imshow("normal", normal)
cv2.imshow("mixed", mixed)
cv2.waitKey()
cv2.destroyAllWindows()