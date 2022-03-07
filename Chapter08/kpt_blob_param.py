# 필터 옵션으로 생성한 SimpleBlobDector 검출기

import cv2
import numpy as np

img = cv2.imread("./img/house.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# BLOB 검출 필터 파라미터 생성
params = cv2.SimpleBlobDetector_Params()

# BLOB를 생성하기 위한 경계 값
# minThreshold에서 maxThreshold를 넘지 않을 때 까지 thresholdStep만큼 증가
params.minThreshold = 10
params.maxThreshold = 240
params.thresholdStep = 5

# 면적 필터 옵션
params.filterByArea = True
# 검출 최소값 설정
params.minArea = 200

# 필터 옵션
params.filterByColor = False            # 밝기 필터
params.filterByConvexity = False        # 볼록 비율 필터
params.filterByInertia = False          # 관성 비율 필터
params.filterByCircularity = False      # 원형 비율 필터

# 필터 파라미터로 BLOB 검출기 생성
detector = cv2.SimpleBlobDetector_create(params)
# 키 포인트 검출
keypoints = detector.detect(gray)
# 키 포인트 그리기
img_draw = cv2.drawKeypoints(img, keypoints, None, None,\
                             cv2.DrawMatchesFlags_DRAW_RICH_KEYPOINTS)

cv2.imshow("Blob with Params", img_draw)
cv2.waitKey(0)
cv2.destroyAllWindows()