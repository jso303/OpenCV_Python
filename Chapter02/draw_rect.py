import cv2
img = cv2.imread("./img/Ch02_img/blank_500.jpg")

cv2.rectangle(img, (50,50), (150,150), (255,0,0))   # 좌상, 우하 좌표로 사각형 그리기
cv2.rectangle(img, (300,300), (100,100), (0,255,0), 10) # 우하, 좌상 좌표로 사각형 그리기

cv2.rectangle(img, (450, 200), (200,450), (0,0,255), -1) # 우상, 좌하 좌표로 사각형 채워 그리기

cv2.imshow("rectangle", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 두 좌표를 연결하여 사각형 그림, 
# (파일 위치, 좌표1, 좌표2, 색, 선 굵기)
# 선 굵기가 -1 이 될 경우 전체를 채운다.
# 늦게 그린 선이 이전에 그린 선을 덮어서 그린다.