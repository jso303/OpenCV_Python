import cv2
import numpy as np
import matplotlib.pylab as plt

# 큐브 영상을 읽어서 HSV로 변환
img = cv2.imread("./img/cube.jpg")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 색상별 영역 지정
blue1 = np.array([90, 50, 50])
blue2 = np.array([120, 255, 255])
green1 = np.array([45, 50, 50])
green2 = np.array([75, 255, 255])
red1 = np.array([0, 50, 50])
red2 = np.array([15, 255, 255])
red3 = np.array([165, 50, 50])
red4 = np.array([180, 255, 255])
yellow1 = np.array([20, 50, 50])
yellow2 = np.array([35, 255, 255])

# 각 색상별 마스크 생성
# 색상 영역(두 번째와 세 번째 인자의 배열 구간)에 포함 될 경우 255(흰색) 값을 할당 하고 아니면 0(검은색)을 할당함
mask_blue = cv2.inRange(hsv, blue1, blue2)
mask_green = cv2.inRange(hsv, green1, green2)
mask_red = cv2.inRange(hsv, red1, red2)
mask_red2 = cv2.inRange(hsv, red3, red4)
mask_yellow = cv2.inRange(hsv, yellow1, yellow2)

# 색상별 마스크로 색상만 추출
# bitwise_and : 둘 다 0(검은색)인 부분만 0으로, 나머지는 세번째 인자 값으로
# bitwise_or : 둘 중 하나만 0(검은색)이여도 0으로
res_blue = cv2.bitwise_and(img, img, mask=mask_blue)
res_green = cv2.bitwise_and(img, img, mask=mask_green)
res_red1 = cv2.bitwise_and(img, img, mask=mask_red)
res_red2 = cv2.bitwise_and(img,img, mask=mask_red2)
res_red = cv2.bitwise_or(res_red1, res_red2)
res_yellow = cv2.bitwise_and(img,img, mask=mask_yellow)

# 추출한 색상 모두 포함한 이미지
all = res_blue + res_green + res_red + res_yellow

imgs = {"original": img, "blue":res_blue, "green":res_green, "red":res_red, "yellow":res_yellow, "all":all}

for i, (k,v) in enumerate(imgs.items()):
    plt.subplot(2,3, i+1)
    plt.title(k)
    plt.imshow(v[:,:,::-1])
    plt.xticks([])
    plt.yticks([])
    
plt.show()