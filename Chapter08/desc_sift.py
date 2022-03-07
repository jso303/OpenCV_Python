# 키 포인트 : 특징이 있는 픽셀의 좌표와 주변 픽셀과의 관계 정보를 지님
# 특징 디스크립터 : 키 포인트 주변 픽셀의 밝기, 색상, 방향, 크기 등의 정보를 지님
# 회전, 크기, 방향 등에 영향 없이 특징을 추출하기 위해 사용

# SIFT로 키 포인트 및 디스크립터 추출
# SIFT는 이미지 피라미드를 이용해 특징 검출을 해결한 알고리즘이다.
# 특허권이 있으므로 상업적 사용은 불가이니 주의

# SIFT는 현 python에서는 특허권으로 인해 설치되어 있지 않아 해당 코드는 작동하지 않음

import cv2
import numpy as np

img = cv2.imread("./img/house.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# SIFT 추출기 생성
sift = cv2.xfeatures2d.SIFT_create()
# 키 포인트 검출과 서술자 계산
keypoints, descriptor = sift.detectAndCompute(gray, None)
print("keypoint:", len(keypoints), "descriptor:", descriptor.shape)
print(descriptor)

# 키 포인트 그리기
img_draw = cv2.drawKeypoints(img, keypoints, None,\
                             flags=cv2.DrawMatchesFlags_DRAW_RICH_KEYPOINTS)

cv2.imshow("SIFT", img_draw)
cv2.waitKey()
cv2.destroyAllWindows()