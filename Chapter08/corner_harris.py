# 해리스 코너 검출
# 소벨 미분으로 엣지를 검출하면서 엣지의 경사도 변화량을 측정해 코너를 검출
# 엣지의 X축, Y축 모든 방향으로 크게 변화하는 것을 코너로 판단
# 원조격 방식으로 현재는 사용되지 않음

import cv2
import numpy as np

img = cv2.imread("./img/house.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 해리스 코너 검출
# cv2.cornerHarris(입력 영상, 이웃 픽셀 범위, 소벨 미분 커널 크기, 코너 검출 상수(0.04~0.06))
corner = cv2.cornerHarris(gray, 2, 3, 0.04)
# 변화량 결과의 최대 값 10% 이상의 좌표 구하기
coord = np.where(corner > 0.1*corner.max())
coord = np.stack((coord[1], coord[0]), axis=-1)

# 코너 좌표에 동그라미 그리기
for x,y in coord:
    cv2.circle(img, (x,y), 5, (0,0,255), 1, cv2.LINE_AA)
    
# 변화량을 영상으로 표현하기 위해서 0~255로 정규화
corner_norm = cv2.normalize(corner, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
# 컬러로 다시 변환
corner_norm = cv2.cvtColor(corner_norm, cv2.COLOR_GRAY2BGR)

# 화면에 검출 화면과 원본 이미지 같이 출력
merged = np.hstack((corner_norm, img))
cv2.imshow("Harris Corner", merged)
cv2.waitKey()
cv2.destroyAllWindows()

