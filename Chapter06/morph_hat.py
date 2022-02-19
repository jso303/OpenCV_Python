# 탑햇, 블랙햇 연산 적용

# 탑햇 : 원본 - 열림            밝기 값이 튀는 부분 강조
# 블랙햇 : 원본 - 닫힘          어두운 부분 강조

import cv2
import numpy as np

img = cv2.imread("./img/moon_gray.jpg")

k = cv2.getStructuringElement(cv2.MORPH_RECT, (9,9))

tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, k)
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, k)

merged = np.hstack((img, tophat, blackhat))
cv2.imshow("tophat, blackhat", merged)
cv2.waitKey(0)
cv2.destroyAllWindows()