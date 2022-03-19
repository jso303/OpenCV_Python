# 16컬러 군집화
# 16컬러만 으로 색상 표현

import cv2
import numpy as np

K = 16      # 군집화 개수(16컬러)
img = cv2.imread("./img/taekwonv1.jpg")
# 군집화를 위한 데이터 구조와 형식 변환
data = img.reshape((-1,3)).astype(np.float32)
# 반복 중지 요건
criteria = (cv2.TermCriteria_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

# 평균 클러스터링 적용
ret, label, center = cv2.kmeans(data,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

# 중심 값을 정수로 변환
center = np.uint8(center)
print(center)

# 각 레이블에 해당하는 중심 값으로 픽셀 값 선택
res = center[label.flatten()]
# 원본 영상의 형태로 변환
res = res.reshape((img.shape))

merged = np.hstack((img, res))
cv2.imshow("KMeans Color", merged)
cv2.waitKey(0)
cv2.destroyAllWindows()