# 사물 영상 중에서 권총 영상 찾기
# 101 가지 종류의 사물들 이미지에서 권총 찾기
# 사진의 총 개수는 9144개

# 해시 매칭은 같은 방향, 크기, 위치를 가진 영상에서 유용함
# 단순히 같은 위치의 픽셀 값 비교를 하기 때문

import cv2
import numpy as np
import glob

img = cv2.imread("./img/pistol.jpg")
cv2.imshow("query", img)

# 비교할 영상들이 있는 경로
search_dir = "./img/101_ObjectCategories"

# 이미지를 16 x 16 크기의 평균 해시로 변환
def img2hash(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.resize(gray, (16,16))
    avg = gray.mean()
    bi = 1 * (gray > avg)
    return bi

# 해밍 거리 측정 함수
def hamming_distance(a,b):
    a = a.reshape(1, -1)
    b = b.reshape(1, -1)
    # 같은 자리의 값이 서로 다른 것들의 합
    distance = (a != b).sum()
    return distance

# 권총 영상의 해시 구하기
query_hash = img2hash(img)

# 이미지 데이터셋 디렉터리의 모든 영상 파일 경로
img_path = glob.glob(search_dir +"/**/*.jpg")
for path in img_path:
    # 데이터셋 영상 한개를 읽고 표시
    img = cv2.imread(path)
    cv2.imshow("searching...", img)
    cv2.waitKey(5)
    # 해당 데이터셋 영상 한 개의 해시
    a_hash = img2hash(img)
    # 해밍 거리 산출
    dst = hamming_distance(query_hash, a_hash)
    
    # 해밍 거리가 25% 이내일 경우 출력
    if dst/256 < 0.25:
        print(path, dst/256)
        cv2.imshow(path, img)
        
# 모든 영상의 해시 판단이 끝나면 searching... 윈도우 종료
cv2.destroyWindow("searching...")
cv2.waitKey(0)
cv2.destroyAllWindows()