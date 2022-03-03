# 동전 개수 세기 워크숍

import cv2
from cv2 import threshold
from cv2 import THRESH_BINARY
from cv2 import THRESH_OTSU
from cv2 import connectedComponents
import numpy as np

img = cv2.imread("./img/coins_connected.jpg")
rows, cols = img.shape[:2]
cv2.imshow("original", img)
cv2.waitKey(0)

# 동전 표면을 흐릿하게 만듬
mean = cv2.pyrMeanShiftFiltering(img, 20, 50)
cv2.imshow("mean", mean)
cv2.waitKey(0)

# 바이너리 이미지(검은색(0)과 흰색(255) 두가지 색으로만 이루어진 이미지)로 변환

# 그레이 스케일로 변환
gray = cv2.cvtColor(mean, cv2.COLOR_BGR2GRAY)
# 가우시안 블러로 노이즈 제거
gray = cv2.GaussianBlur(gray, (3,3), 0)
# 오츠 알고리즘으로 최적의 경계 값으로 바이너리 이미지 생성
_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
cv2.imshow("thresh", thresh)
cv2.waitKey(0)

# 동전이 모여 있기 때문에 경계 구분이 어려움
# 동전과 배경의 거리 측정
dst = cv2.distanceTransform(thresh, cv2.DIST_L2, 3)
# 배경에서 멀어질 수록 흰색(255)에 가까운 색으로, 배경은 검은색(0)
dst = (dst / (dst.max() - dst.min()) * 255 ).astype(np.uint8)
cv2.imshow("dst", dst)
cv2.waitKey(0)

# 팽창 적용
# (50,50) 픽셀 내에서 가장 큰 값으로 색을 채운 값 계산
# (50,50) 은 동전 정도의 크기
localMx = cv2.dilate(dst, np.ones((50,50), np.uint8))

# 로컬 최대값을 저장할 배열 생성
lm = np.zeros((rows, cols), np.uint8)

# 로컬 최대값과 기존 값이 같다면 255로 색 지정
# 동전의 중심부를 찾는 것
lm[(localMx==dst) & (dst != 0)] = 255
cv2.imshow("localMx", lm)
cv2.waitKey(0)


# 로컬 최대 값으로 색 채우기(흰색(255))
# 로컬 최대 값이 있는 좌표 구하기
seeds = np.where(lm == 255)
seed = np.stack( (seeds[1], seeds[0]), axis=-1)

# 색 채우기를 위한 마스크 생성
fill_mask = np.zeros((rows+2, cols+2), np.uint8)
for x,y in seed:
    # 로컬 최대 값을 시드로 평균 시프트(동전 흐리게 한) 영상에 색 채우기 적용
    ret = cv2.floodFill(mean, fill_mask, (x,y), (255,255,255), (10,10,10), (10,10,10))
cv2.imshow("floodFill", mean)
cv2.waitKey(0)


# 색 채우기 한 영상에 바이너리 이미지로 변환, 동전과 배경의 거리 측정 (위에서 한 작업 재 작업)
gray = cv2.cvtColor(mean, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5,5), 0)
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
dst = cv2.distanceTransform(thresh, cv2.DIST_L2, 5)
dst = ( (dst / dst.max() - dst.min())* 255).astype(np.uint8)
cv2.imshow("dst2", dst)
cv2.waitKey(0)

# 거리 변환 결과 값에서 50% 값을 넘으면 확실한 전경으로 설정 (배경은 0, 배경에서 멀어질 수록 255에 가까워짐)
ret, sure_fg = cv2.threshold(dst, 0.5*dst.max(), 255, 0)
cv2.imshow("sure_fg", sure_fg)
cv2.waitKey(0)

# 거리 변환 결과 값을 반전하고 다시 거리 값 측정 후 30% 값을 넘으면 확실한 배경으로 설정
_, bg_th = cv2.threshold(dst, 0.3*dst.max(), 255, cv2.THRESH_BINARY_INV)
bg_dst = cv2.distanceTransform(bg_th, cv2.DIST_L2, 5)
bg_dst = ( (bg_dst / (bg_dst.max() - bg_dst.min())) * 255).astype(np.uint8)
ret, sure_bg = cv2.threshold(bg_dst, 0.3*bg_dst.max(), 255, cv2.THRESH_BINARY)
cv2.imshow("sure_bg", sure_bg)
cv2.waitKey(0)


# 불확실한 영역 설정(확실한 배경(확실한 전경+불확실한 전경)을 반전해서 확실한 전경을 빼기\
#                   == 불확실한 전경)
ret, inv_sure_bg = cv2.threshold(sure_bg, 127, 255, cv2.THRESH_BINARY_INV)
unkown = cv2.subtract(inv_sure_bg, sure_fg)
cv2.imshow("unkown", unkown)
cv2.waitKey(0)

# 연결된 요소 레이블링(분류하고 라벨을 붙이는 작업)
_, markers = cv2.connectedComponents(sure_fg)

# 레이블링을 1씩 증가시키고 레이블을 알 수 없는 영역을 0번 레이블로 설정
markers = markers+1
markers[unkown == 255] = 0
print("워터셰드 전:", np.unique(markers))
colors = []
marker_show = np.zeros_like(img)
for mid in np.unique(markers):  # 마커 아이디 개수만큼 반복
    color = [int(j) for j in np.random.randint(0, 255, 3)]
    colors.append((mid, color))
    marker_show[markers==mid] = color
    coords = np.where(markers==mid)
    x,y = coords[1][0], coords[0][0]
    cv2.putText(marker_show, str(mid), (x+20, y+20), cv2.FONT_HERSHEY_PLAIN, 2, (255,255,255))
cv2.imshow("before", marker_show)
cv2.waitKey(0)

# 레이블링이 완성된 마커로 워터셰드 적용
markers = cv2.watershed(img, markers)
print("워터셰드 후:", np.unique(markers))

for mid, color in colors:
    marker_show[markers==mid] = color
    coords = np.where(markers==mid)
    if coords[0].size <= 0:
        continue
    x,y = coords[1][0], coords[0][0]
    cv2.putText(marker_show, str(mid), (x+20, y+20), cv2.FONT_HERSHEY_PLAIN, 2, (255,255,255))

marker_show[markers==-1] = (0,255,0)
cv2.imshow("watershed marker", marker_show)
cv2.waitKey(0)

img[markers==-1] = (0,255,0)
cv2.imshow("watershed:", img)
cv2.waitKey(0)

# 동전 추출을 위한 마스킹 생성
mask = np.zeros((rows, cols), np.uint8)
mask[markers!=1] = 255

# 배경 지우기
nobg = cv2.bitwise_and(img, img, mask=mask)
# 동전만 있는 라벨 생성(배경(1), 경계(-1)가 둘 다 없는)
coin_label = [l for l in np.unique(markers) if (l != 1 and l != -1)]

# 동전 라벨을 순회하면서 동전 영역만 추출
for i, label in enumerate(coin_label):
    mask[:,:] = 0
    # 해당 동전 추출 마스크 생성
    mask[markers == label] = 255
    # 동전 영역만 마스크로 추출 
    coins = cv2.bitwise_and(img, img, mask=mask)
    contour, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    
    # 동전을 감싸는 사각형 좌표
    x,y,w,h = cv2.boundingRect(contour[0])
    # 동전 영역만 추출해서 출력
    coin = coins[y:y+h, x:x+w]
    cv2.imshow("coin%d" %(i+1), coin)
    cv2.imwrite("./img/coin_test/coin%d.jpg" %(i+1), coin)
cv2.waitKey()
cv2.destroyAllWindows()