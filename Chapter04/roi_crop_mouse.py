import cv2
import numpy as np

isDragging = False                  # 마우스 드래그 상태 저장
x0, y0, w, h = -1,-1,-1,-1          # 영역 선택 좌표 저장 초기화
blue, red = (255,0,0), (0,0,255)    # 색상 값

def onMouse(event,x,y,flags,param):         # 마우스 이벤트 핸들 함수
    global isDragging, x0, y0, img          # global : 전역변수 참조
    if event == cv2.EVENT_LBUTTONDOWN:  # 마우스 왼쪽 버튼을 누른 경우
        isDragging = True               # 드래그 상태 = True
        x0 = x
        y0 = y
    elif event == cv2.EVENT_MOUSEMOVE:  # 마우스 움직임
        if isDragging:                  # 드래그 중
            img_draw = img.copy()       # 이미지 복제를 한다.
            cv2.rectangle(img_draw, (x0, y0), (x,y), blue, 2)   # 드래그 진행중인 영역 표시 (파랑)
            cv2.imshow("img", img_draw)                         # 사각형으로 표시된 그림 화면 출력
    elif event == cv2.EVENT_LBUTTONUP:  # 마우스 왼쪽 버튼을 뗀 경우
        if isDragging:
            isDragging = False          # 드래그 상태 = False
            w = x - x0                  # 드래그 한 영역 폭 계산
            h = y - y0                  # 드래그 한 영역 높이 계산
            print("x:%d, y:%d, w:%d, h:%d" %(x0, y0, w, h))
            if w > 0 and h > 0:         # 드래그 한 영역의 폭, 높이가 음수일 경우
                img_draw = img.copy()   # 사각형 그림 표현을 위한 이미지 복제 
                cv2.rectangle(img_draw, (x0,y0), (x,y), red, 2) # 드래그 한 영역을 빨간색 사각형으로 표시
                cv2.imshow("img", img_draw)
                roi = img[y0:y0+h, x0:x0+w]             # 선택 영역 roi로 지정
                cv2.imshow("cropped", roi)              # roi 영역만 새 창으로 표시
                cv2.moveWindow("cropped", 0,0)          # 새 창을 화면 좌측 상단으로 이동
                cv2.imwrite("./cropped.jpg", roi)       # roi 영역 파일로 저장
                print("croped.")
            else:                                       # 드래그 영역이 잘못된 경우 원본 이미지 출력
                cv2.imshow("img", img)
                print("좌측 상단에서 우측 하단으로 영역을 드래그하세요.")
            
img = cv2.imread("./img/sunset.jpg")
cv2.imshow("img", img)
cv2.setMouseCallback("img", onMouse)
cv2.waitKey()
cv2.destroyAllWindows()