import cv2

title = "mouse event"
img = cv2.imread("./img/Ch02_img/blank_500.jpg")
cv2.imshow(title, img)

def onMouse(event, x, y, flags, param):         # 마우스 콜백 함수 구현
    print(event, x, y, )                        # 마우스 위치 파라미터 출력
    if event == cv2.EVENT_LBUTTONDOWN:          # 왼쪽 버튼 누를 경우
        cv2.circle(img, (x,y), 30, (0,0,0), -1) # 지름이 30픽셀인 꽉찬 검은색 원을 이미지에 그림
        cv2.imshow(title, img)                  # 원이 그려진 이미지로 다시 표시
        
cv2.setMouseCallback(title, onMouse)            # 마우스 콜백 함수를 GUI 윈도에 등록

while True:
    if cv2.waitKey(0) & 0xFF == 27:             # esc로 종료
        break
cv2.destroyAllWindows()