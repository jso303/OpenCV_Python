# 삼각형 어핀 변환

import cv2
import numpy as np

img = cv2.imread("./img/taekwonv1.jpg")
img2 = img.copy()
draw = img.copy()

# 변환 전,후 삼각형 좌표
pts1 = np.float32([[188,14], [85,202], [294,216]])
pts2 = np.float32([[128,40], [85,307], [306,167]])

# 변환 전,후의 삼각형을 완전히 감싸는 사각형 좌표 구하기
x1,y1,w1,h1 = cv2.boundingRect(pts1)
x2,y2,w2,h2 = cv2.boundingRect(pts2)

# 사각형 좌표를 이용해 관심영역 설정
roi1 = img[y1:y1+h1, x1:x1+w1]
roi2 = img2[y2:y2+h2, x2:x2+w2]

# 관심영역을 기준으로 좌표 계산
offset1 = np.zeros((3,2), dtype=np.float32)
offset2 = np.zeros((3,2), dtype=np.float32)
for i in range(3):
    offset1[i][0], offset1[i][1] = pts1[i][0] -x1, pts1[i][1]-y1
    offset2[i][0], offset2[i][1] = pts2[i][0] -x2, pts2[i][1]-y2
    
# 관심영역을 주어진 삼각형 좌표로 어핀 변환    
mtrx = cv2.getAffineTransform(offset1, offset2)
warped = cv2.warpAffine(roi1, mtrx, (w2, h2), None, \
                        cv2.INTER_LINEAR, cv2.BORDER_REFLECT_101)

# 어핀 변환 후 삼각형만 골라 내기 위한 마스크 생성
mask = np.zeros((h2,w2), dtype = np.uint8)
cv2.fillConvexPoly(mask, np.int32(offset2), (255))

# 삼각형 영역만 마스킹해서 기존 이미지에 합성
warped_masked = cv2.bitwise_and(warped, warped, mask=mask)
roi2_masked = cv2.bitwise_and(roi2, roi2, mask=cv2.bitwise_not(mask))
roi2_masked = roi2_masked + warped_masked
img2[y2:y2+h2, x2:x2+w2] = roi2_masked

# 관심영역과 삼각형에 선을 그려 표시를 내 출력 (사각형 : 녹색, 삼각형 : 파란색)
cv2.rectangle(draw, (x1,y1), (x1+w1,y1+h1), (0,255,0),1)
cv2.polylines(draw, [pts1.astype(np.int32)], True, (255,0,0), 1)
cv2.rectangle(img2, (x2,y2), (x2+w2, y2+h2), (0,255,0), 1)
cv2.imshow("origin", draw)
cv2.imshow("warped triangle", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()