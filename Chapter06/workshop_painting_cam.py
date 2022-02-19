# 웹캠 영상을 스케치한 그림처럼 보여주는 카메라 제작

# 스케치한 영상, 스케치에 물감까지 칠한 영상 2가지 만들기

# 처리 순서
# cv2.GausianBlur()로 노이즈 제거
# cv2.Laplacian()로 엣지 습득
# 스레시홀드로 경계 이외의 것들 제거 후 반전하기(스케치한 모습처럼 표현됨)

# 물감 영상은 스케치 영상에 컬러영상에 블러 처리한 후 합성하면 됨
# 블러 처리는 cv2.blur() 사용

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while (cap.isOpened()):
    ret, frame = cap.read()
    
    flip_frame = cv2.flip(frame, 1)     # 좌우 반전
    # 사이즈 절반으로 축소
    resize_frame = cv2.resize(flip_frame, None, fx=0.5, fy=0.5, \
                              interpolation=cv2.INTER_AREA)

    # esc 키로 종료
    if cv2.waitKey(1) == 27:
        break
    
    img_gray = cv2.cvtColor(resize_frame, cv2.COLOR_BGR2GRAY)
    img_gray = cv2.GaussianBlur(img_gray, (9,9), 0)
    
    edges = cv2.Laplacian(img_gray, -1, None, 5)
    
    ret, sketch = cv2.threshold(edges, 70, 255, cv2.THRESH_BINARY_INV)
    
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3,3))
    sketch = cv2.erode(sketch, kernel)
    sketch = cv2.medianBlur(sketch, 5)
    
    img_sketch = cv2.cvtColor(sketch, cv2.COLOR_GRAY2BGR)
    
    img_paint = cv2.blur(resize_frame, (10,10))
    img_paint = cv2.bitwise_and(img_paint, img_paint, mask=sketch)
    
    merged = np.hstack((img_sketch, img_paint))
    cv2.imshow("camera", merged)
    
cap.release()
cv2.destroyAllWindows()
