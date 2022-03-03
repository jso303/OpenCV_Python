# 마우스와 워터셰드로 배경 분리
# 워터셰드 : 경계를 찾는 방법
# 밝은 픽셀은 높은 곳에, 어두운 픽셀은 낮은 곳에 있다고 가정하는 2차원 지형으로 생각
# 골짜기에 물을 채워 물이 봉우리를 넘어 만나는 지점을 경계로 찾는 방식

import cv2
import numpy as np

img = cv2.imread("./img/taekwonv1.jpg")
rows, cols = img.shape[:2]
img_draw = img.copy()

# 마커 생성, 모든 요소 초기화
marker = np.zeros((rows, cols), np.int32)
markerId = 1            # 마커 아이디
colors = []             # 마커를 선택한 픽셀의 색상 값 저장
isDragging = False      # 드래그 여부 확인 변수

# 마우스 이벤트 처리 함수
def onMouse(event, x, y, flags, param):
    global img_draw, marker, markerId, isDragging
    if event == cv2.EVENT_LBUTTONDOWN:      # 왼쪽 마우스 다운
        isDragging = True                   # 드래그 시작
        colors.append((markerId, img[y,x]))   # 현재 마커 아이디와 현 위치의 색상 값을 쌍으로 저장
    elif event == cv2.EVENT_MOUSEMOVE:      # 마우스 움직임
        if isDragging:
            marker[y,x] = markerId          # 마커 아이디를 드래그 하는 동안 통일
            cv2.circle(img_draw, (x,y), 3, (0,0,255), -1)   # 마커 표시를 빨간색 점으로 표시해 출력
            cv2.imshow("watershed", img_draw)
    elif event == cv2.EVENT_LBUTTONUP:      # 왼쪽 마우스 업
        if isDragging:
            isDragging = False              # 드래그 종료
            markerId +=1                    # 마커 아이디 1 증가
    
    elif event == cv2.EVENT_RBUTTONDOWN:    # 오른쪽 마우스 다운
        # 워터셰드 적용
        # cv2.watershed(입력 영상, 마커)
        cv2.watershed(img, marker)
        img_draw[marker == -1] = (0,255,0)
        for mid, color in colors:
            img_draw[marker==mid] = color
        cv2.imshow("watershed", img_draw)
    
cv2.imshow("watershed", img)
cv2.setMouseCallback("watershed", onMouse)
cv2.waitKey()
cv2.destroyAllWindows()
            