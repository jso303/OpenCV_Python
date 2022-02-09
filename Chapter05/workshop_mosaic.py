# 모자이크 처리하기
# 마우스로 영역을 선택하여 모자이크 처리함
# 마우스로 선택은 cv2.selectROI로 관심영역 선택
# 보간법 알고리즘에서 cv2.INTER_AREA 사용
# 영역을 작게 축소했다가 다시 확대하는 방식으로 모자이크 처리
# 축소하면 픽셀의 색이 평균값으로 통일됨

import cv2
import numpy as np

rate = 15               # 모자이크 축소 비율(1/rate)    # 1이 기본, 높아질 수록 저 해상도가 됨
win_title = "mosaic"    # 창 제목
img = cv2.imread("./img/taekwonv1.jpg")

while True:
    x,y,w,h = cv2.selectROI(win_title, img, False)  # 관심영역 선택
    if w and h:
        roi = img[y:y+h, x:x+w]     # 관심영역 선택
        roi = cv2.resize(roi, (w//rate, h//rate))   # 1/rate 비율로 축소
        roi = cv2.resize(roi, (w,h), interpolation=cv2.INTER_AREA)  # 원래크기로 확대
        img[y:y+h, x:x+w] = roi         # 원본 이미지에 적용
        cv2.imshow(win_title, img)
    else:
        break
cv2.destroyAllWindows()