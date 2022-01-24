import cv2
file_path = "./img/Ch02_img/girl.jpg"
img = cv2.imread(file_path)                                 # 이미지를 기본 값으로 받기
img_gray = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)      # 이미지를 흑백으로 받기

cv2.namedWindow("origin", cv2.WINDOW_AUTOSIZE)              # 원래 크기로 이미지 창 생성
cv2.namedWindow("gray", cv2.WINDOW_NORMAL)                  # 임의의 크기로 이미지 창 생성

cv2.imshow("origin", img)           # "origin" 창에 (기본값으로 받았던)이미지 표시
cv2.imshow("gray", img_gray)        # "gray" 창에 (흑백으로 받았던)이미지 표시

cv2.moveWindow("origin", 0,0)       # 창 위치 변경
cv2.moveWindow("gray", 100,100)     # 창 위치 변경

cv2.waitKey(0)                          # 아무키나 누르면
cv2.resizeWindow("origin", 200, 200)    # 창 크기 변경 (이미지 변경 불가, 그림이 짤려서 나옴)
cv2.resizeWindow("gray", 100, 100)      # 창 크기 변경 (변경 가능)

cv2.waitKey(0)                          
cv2.destroyWindow("gray")           # "gray" 창 닫기

cv2.waitKey(0)
cv2.destroyAllWindows()                 # 모든 창 닫기