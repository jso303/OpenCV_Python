# 필터를 이용해 선택 영역을 모자이크 처리하기

# 5장에서는 특정 영역을 축소한 뒤 확대하여 모자이크 처리하였음

# 선택한 영역을 평균 블러링 필터를 적용하여 모자이크 처리하면 됨

import cv2

win_title = "mosaic"
img = cv2.imread("./img/taekwonv1.jpg")

while True:
    x,y,w,h = cv2.selectROI(win_title, img, False)
    if w > 0 and h > 0:
        roi = img[y:y+h, x:x+w]
        roi = cv2.blur(roi, (20,20))
        img[y:y+h, x:x+w] = roi
        cv2.imshow(win_title, img)
    else:
        break

cv2.destroyAllWindows()