# 관심영역 지정을 위함 함수가 기본으로 제공이 된다.
# roi_crop_mouse.py 파일과 같이 직접 만들 필요없이 간단히 작성 가능.

import cv2
import numpy as np

img = cv2.imread("./img/sunset.jpg")

x,y,w,h = cv2.selectROI("img", img, False)
if w and h:
    roi = img[y:y+h, x:x+w]
    cv2.imshow("cropped", roi)          # ROI 지정 영역을 새창으로 표시
    cv2.moveWindow("cropped", 0,0)      # 새 창을 화면 좌측 상단으로 이동
    cv2.imwrite("./cropped2.jpg", roi)   # ROI 영역만 파일로 저장
    
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()