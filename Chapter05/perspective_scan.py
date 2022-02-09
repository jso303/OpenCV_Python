# 마우스와 원근 변환으로 문서 스캔 효과 내기

import cv2
import numpy as np

win_name = "scanning"
img = cv2.imread("./img/paper.jpg")
print(type(img.shape))
rows,cols = img.shape[:2]
draw = img.copy()
pts_cnt = 0
pts = np.zeros((4,2), dtype=np.float32)

# 마우스 콜백 함수 구현
def onMouse(event, x, y, flags, param):
    global pts_cnt                      # 마우스로 찍은 점 갯수 저장
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(draw, (x,y), 10, (0,255,0), -1)  # 마우스로 찍은 점 녹색원으로 표시
        cv2.imshow(win_name, draw)
        
        pts[pts_cnt] = [x,y]    # 마우스 좌표 저장
        pts_cnt+=1
        if pts_cnt == 4:
            sm = pts.sum(axis=1)            # 4쌍의 좌표들 각각 x+y 계산
            diff = np.diff(pts, axis = 1)   # 4쌍의 좌표들 각각 x-y 계산
            
            topLeft = pts[np.argmin(sm)]        # x,y 합이 가장 작은 값이 좌상단 좌표
            bottomRight = pts[np.argmax(sm)]    # x,y 합이 가장 큰 값이 우하단 좌표
            topRight = pts[np.argmin(diff)]     # x,y 차가 가장 작은 값이 우상단 좌표
            bottomLeft = pts[np.argmax(diff)]   # x,y 차가 가장 큰 값이 좌하단 좌표
            
            # 변환 전 4개 좌표
            pts1 = np.float32([topLeft, topRight, bottomRight, bottomLeft])
            
            # 변환 후 영상에 사용될 서류의 폭과 높이 계산
            # 좌우 값 차이 중 큰 값으로 폭
            # 상하 값 차이 중 큰 값으로 높이
            # [0] : x 좌표(폭 계산에 사용), [1] : y 좌표(높이 계산에 사용)
            w1 = abs(bottomRight[0] - bottomLeft[0])    # 상단 좌우 좌표간의 거리
            w2 = abs(topRight[0] - topLeft[0])          # 하당 좌우 좌표간의 거리
            h1 = abs(topRight[1] - bottomRight[1])      # 우측 상하 좌표간의 거리
            h2 = abs(topLeft[1] - bottomLeft[1])        # 좌측 상하 좌표간의 거리
            width = max([w1, w2])                       # 두 좌우 거리간의 최대값이 서류의 폭
            height = max([h1, h2])                      # 두 상하 거리간의 최대값이 서류의 높이
            print(type(width))
            print(type(height))
            
            # 변환 후 4개 좌표
            pts2 = np.float32([[0,0], [width-1, 0], [width-1, height-1], [0, height-1]])
            
            # 변환 행렬 계산
            mtrx = cv2.getPerspectiveTransform(pts1, pts2)
            
            # 원근 변환으로 폭, 높이를 동일한 수준으로 맞춰줌
            result = cv2.warpPerspective(img, mtrx, (width, height))
            cv2.imshow("scanned", result)
            
cv2.imshow(win_name, img)
cv2.setMouseCallback(win_name, onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()