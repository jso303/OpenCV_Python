# 마우스와 그랩컷으로 배경 분리
# 1차로 마우스 드래그로 객체 사각형 내에 들어가도록 지정
# 분명한 전경은 컨트롤 키를 누른 상태로 마우스 움직여 지정
# 분명한 배경은 시프트 키를 누른 상태로 마우스 움직여 지정

import cv2
import numpy as np

img = cv2.imread("./img/taekwonv1.jpg")
img_draw = img.copy()
mask = np.zeros(img.shape[:2], dtype=np.uint8)
rect = [0,0,0,0]
# 그랩컷 초기모드
mode = cv2.GC_EVAL

# 배경 및 전경 모델 버퍼
bgdmodel = np.zeros((1,65), np.float64)
fgdmodel = np.zeros((1,65), np.float64)

# 마우스 이벤트 처리 함수
def onMouse(event, x, y, flags, param):
    global mouse_mode, rect, mask, mode
    if event == cv2.EVENT_LBUTTONDOWN:      # 왼쪽 마우스 다운
        if flags <= 1:                      # 아무 키도 안 눌렀으면
            mode = cv2.GC_INIT_WITH_RECT   # 드래그 시작, 사각형 모드
            rect[:2] = x,y                  # 시작 좌표 저장
        
    # 마우스가 움직이고 왼쪽 버튼이 눌러진 상태    
    elif event == cv2.EVENT_MOUSEMOVE and flags & cv2.EVENT_FLAG_LBUTTON:
        if mode == cv2.GC_INIT_WITH_RECT:   # 드래그 진행 중일 때
            img_temp = img.copy()
            # 드래그 사각형을 화면에 표시(녹색)
            cv2.rectangle(img_temp, (rect[0], rect[1]), (x,y), (0,255,0), 2)
            cv2.imshow("img", img_temp)
            
        elif flags > 1:                     # 키가 눌러진 상태
            mode = cv2.GC_INIT_WITH_MASK
            if flags & cv2.EVENT_FLAG_CTRLKEY:  # 컨트롤 키를 누른 경우(전경 표시)
                # 흰색 점으로 화면에 표시
                cv2.circle(img_draw, (x,y), 3, (255,255,255), -1)
                cv2.circle(mask, (x,y), 3, cv2.GC_FGD, -1)
            if flags & cv2.EVENT_FLAG_SHIFTKEY: # 쉬프트 키를 누른 경우(배경 표시)
                # 검은색 점으로 화면에 표시
                cv2.circle(img_draw, (x,y), 3, (0,0,0), -1)
                cv2.circle(mask, (x,y), 3, cv2.GC_BGD, -1)
            cv2.imshow("img", img_draw)
    elif event == cv2.EVENT_LBUTTONUP:      # 왼쪽 버튼을 뗀 상태
        if mode == cv2.GC_INIT_WITH_RECT:   # 사각형 그리기 종료
            rect[2:] = x,y                  # 사각형 마지막 좌표 수집
            # 사각형을 그려 화면에 출력
            cv2.rectangle(img_draw, (rect[0], rect[1]), (x,y), (255,0,0), 2)
            cv2.imshow("img", img_draw)
            
        # 그랩컷 적용
        # cv2.grabCut(입력 영상, 배경과 전경을 구분하는 값, 전경이 있을 것으로 추측되는 영역 좌표,\
        #             함수 내에서 사용할 임시 배열 버퍼, 반복 횟수, 동작 방법)
        cv2.grabCut(img, mask, tuple(rect), bgdmodel, fgdmodel, 1, mode)
        img2 = img.copy()
        # 마스크에 확실한 배경과 배경으로 예측되는 영역을 0(검은색)으로 채우기
        img2[(mask==cv2.GC_BGD) | (mask==cv2.GC_PR_BGD)] = 0
        cv2.imshow("grabcut", img2)
        mode = cv2.GC_EVAL
            
cv2.imshow("img", img)
cv2.setMouseCallback("img", onMouse)
while True:
    if cv2.waitKey(0) & 0xFF == 27:
        break
cv2.destroyAllWindows()
                    