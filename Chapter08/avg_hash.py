# 평균 해시 매칭
# 영상을 특정 크기로 축소한 뒤 픽셀 전체의 평균 값을 구해서
# 평균보다 작은 값(어두운 값(검은색 0))은 0, 평균보다 큰 값(밝은 값(흰색은 255))은 1로 구성
# 이렇게 나온 0/1 값들을 기준으로 유사도를 비교함

# 권총을 평균 해시로 변환

import cv2

img = cv2.imread("./img/pistol.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 16 x 16 크기로 축소
gray = cv2.resize(gray, (16,16))
# 영상의 평균 값 구하기
avg = gray.mean()

# 평균 값을 기준으로 0과 1로 변환
bin = 1 * (gray > avg)
print(bin)

# 2진수 문자열을 16진수 문자열로 변환
# 2진수 숫자가 너무 길어 보기가 불편하면 10진수나 16진수로 변환해서 비교해도 된다.
dhash = []
for row in bin.tolist():
    s = "".join([str(i) for i in row])
    dhash.append("%02x"%(int(s,2)))
dhash = "".join(dhash)
print(dhash)

cv2.imshow("pistol", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
