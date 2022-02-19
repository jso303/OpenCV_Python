# 기존 2장에서 video_cam_resize.py 파일에서 배운 방식인 
# set의 경우 카메라에서 지원하는 범위 값만 사용 가능

# 크기 조정 resize로 처리하는 법, 캠화면이 좌우 반전이 되어 출력되는 것 수정

import cv2

cap = cv2.VideoCapture(0)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)                   # 프레임 폭 값 구하기
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)                 # 프레임 높이 값 구하기
print("Original width : %d, height : %d" %(width,height))


while(cap.isOpened()):
    ret, frame = cap.read()
    
    # cv2.flip(입력 영상, 반전 할 방향)         # 0: x축 뒤집기, 1: y축 뒤집기, -1 두축 다 뒤집기
    # cv2.resize(입력 영상, 결과 이미지 크기, 보간법)
    if ret:
        filp_frame = cv2.flip(frame, 1)
        resize_frame = cv2.resize(filp_frame, dsize=(320,240), interpolation=cv2.INTER_LINEAR)
        cv2.imshow("camera", resize_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()