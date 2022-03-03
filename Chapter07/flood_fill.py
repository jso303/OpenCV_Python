# 마우스로 색 채우기

import cv2
import numpy as np

img = cv2.imread("./img/taekwonv1.jpg")
rows, cols = img.shape[:2]

# 마스크 생성, 원래 이미지 보다 2픽셀 크게(floodFill 함수에서 사용을 위해)
mask = np.zeros((rows+2, cols+2), np.uint8)
# 채우기에 사용할 색(흰색)
newVal = (255,255,255)
# 최소/최대 차이 값
loDiff, upDiff = (10,10,10), (10,10,10)

# 마우스 이벤트 처리 함수
def onMouse(event, x, y, flags, param):
    global mask, img
    if event == cv2.EVENT_LBUTTONUP:
        seed = (x,y)
        # 색 채우기 적용
        # cv2.floodFill(입력 영상, 입력 영상보다 2x2 픽셀이 더 큰 배열, 채우기 시작할 좌표,\
        #               채우기에 사용할 색, 채우기 진행할 최소, 최대 차이)
        retval = cv2.floodFill(img, mask, seed, newVal, loDiff, upDiff)
        cv2.imshow("img", img)
        
cv2.imshow("img", img)
cv2.setMouseCallback("img", onMouse)
cv2.waitKey()
cv2.destroyAllWindows()