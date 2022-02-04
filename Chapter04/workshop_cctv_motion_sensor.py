# 모션 감지 CCTV

# 카메라의 차 영상으로 움직임을 감지하고 움직임이 있는 영역을 표시하는 프로그램 제작하기
# 달라진 픽셀 값이 특정 기준치 보다 많은 경우에 움직임이 있는걸로 간주

import cv2
import numpy as np

# 감도 설정
thresh = 10         # 달라진 픽셀 값 기준치 설정
max_diff = 5        # 달라진 픽셀 수 기준치 설정

# 카메라 캡션 장치 준비
a, b, c = None, None, None
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 320)

# 프레임 읽기 (a -> b -> c 순으로 읽으면서 처리시간동안 움직임이 있으면 값이 달라짐)
if cap.isOpened():
    ret, a = cap.read()
    ret, b = cap.read()
    
    while ret:
        ret, c = cap.read()
        draw = c.copy()     # c 값을 출력 영상에 사용하기 위해 복제
        if not ret:
            break
        
        # 3개의 영상을 그레이 스케일로 변환(영상 처리량을 줄이기 위함)
        a_gray = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
        b_gray = cv2.cvtColor(b, cv2.COLOR_BGR2GRAY)
        c_gray = cv2.cvtColor(c, cv2.COLOR_BGR2GRAY)
        
        # a-b, b-c 절대 값 차 구하기
        diff1 = cv2.absdiff(a_gray, b_gray)
        diff2 = cv2.absdiff(b_gray, c_gray)
        
        # 스레시홀드로 기준치 이내의 차이는 무시 (기준치를 만족하면 255(흰색)으로 채움)
        ret, diff1_t = cv2.threshold(diff1, thresh, 255, cv2.THRESH_BINARY)
        ret, diff2_t = cv2.threshold(diff2, thresh, 255, cv2.THRESH_BINARY)
        
        # 두 영상의 차이가 모두 발견된 경우
        diff = cv2.bitwise_and(diff1_t, diff2_t)
        
        # 열림 연산으로 노이즈 제거
        k = cv2.getStructuringElement(cv2.MORPH_CROSS, (3,3))
        diff = cv2.morphologyEx(diff, cv2.MORPH_OPEN, k)
        
        # 차이가 발생한 픽셀이 개수 판단 후 사각형 그리기
        diff_cnt = cv2.countNonZero(diff)
        if diff_cnt > max_diff:
            nzero = np.nonzero(diff)        # 차이가 0이 아닌 픽셀의 좌표 얻기
            # 좌표의 최소 최대값을 기준으로 녹색 사각형을 만듬
            cv2.rectangle(draw, (min(nzero[1]), min(nzero[0])),\
                (max(nzero[1]), max(nzero[1])), (0,255,0), 2)
            # if문 실행시 Motion Detented 문구를 (10,30) 픽셀 위치에 표시
            cv2.putText(draw, "Motion Detected", (10,30),\
                cv2.FONT_HERSHEY_DUPLEX, 0.5, (0,0,255))
            
        stacked = np.hstack((draw, cv2.cvtColor(diff, cv2.COLOR_GRAY2BGR)))
        cv2.imshow("motion sensor", stacked)
        
        a = b
        b = c
        
        if cv2.waitKey(1) & 0xFF == 27:
            break