# 연결된 영역 레이블링
# 같은 영역 찾아 칠하기

import cv2
import numpy as np

img = cv2.imread("./img/shapes_donut.png")
img2 = np.zeros_like(img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, th = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# 연결된 요소 레이블링 적용
# cv2.connectedComponents(입력 영상)
cnt, labels = cv2.connectedComponents(th)

# 레이블 개수만큼 순회
for i in range(cnt):
    # 레이블이 같은 영역에 랜덤한 색상 적용
    img2[labels==i] = [int(j) for j in np.random.randint(0,255,3)]
    
merged = np.hstack((img,img2))
cv2.imshow("connected", merged)
cv2.waitKey()
cv2.destroyAllWindows()