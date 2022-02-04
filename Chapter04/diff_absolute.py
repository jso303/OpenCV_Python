# 차 영상으로 도면의 차이 찾아내기
# img1 과 img2의 차이점 찾기

import cv2
import numpy as np

# 두 이미지를 불러오고 그레이 스케일로 변환
img1 = cv2.imread("./img/robot_arm1.jpg")
img2 = cv2.imread("./img/robot_arm2.jpg")
img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# 두 영상의 절대 값 차 연산
diff = cv2.absdiff(img1_gray, img2_gray)

# 차 영상의 극대화를 위해 스레시홀드 처리 및 컬러로 변환
_, diff = cv2.threshold(diff, 1, 255, cv2.THRESH_BINARY)    # 1보다 큰 값(차이가 존재하는 값)을 255로 변환
diff_red = cv2.cvtColor(diff, cv2.COLOR_GRAY2BGR)           # 컬러로 변환
diff_red[:,:,2] = 0                                         # blue : [:,:,0], green : [:,:,1], red : [:,:,2]

spot = cv2.bitwise_xor(img2, diff_red)          # bitwise_xor 연산으로 차이가 있는 영역을 빨간색으로 표시 

cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.imshow("diff", diff)
cv2.imshow("spot", spot)
cv2.waitKey()
cv2.destroyAllWindows()