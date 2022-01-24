import cv2

video_file = "./img/Ch02_img/test01.mp4"   # 동영상 파일 경로

cap = cv2.VideoCapture(video_file)              # 동영상 캡처 객체 생성
if cap.isOpened():                              # 캡처 객체 초기화 확인
    while True:                                 
        ret, img = cap.read()                   # 다음 프레임 읽기
        if ret:                                 # 프레임 읽기 정상
            cv2.imshow(video_file, img)         # 화면에 표시
            cv2.waitKey(25)                     # 25ms 지연(40fps)
        else:                                   # 다음 프레임을 읽을 수 없으면
            break                               # 재생 종료
    else:
        print("can't open video")               # 캡처 객체 초기화 실패
cap.release()                                   # 캡처 자원 반납
cv2.destroyAllWindows()

# 화면에 지연을 주는 이유는 너무 빠르면 눈으로 보기 힘들기 때문에 다음 프레임으로 넘어가는
# 시간에 지연을 주어 인식할 수 있도록 하는것이다.
# 지연시간 = 1000 / fps
# 즉, 40 fps는 25ms의 지연시간을 가진다.
# 영상의 프레임 속도를 확인하려면 [파일 우클릭 - 속성 - 자세히] 에서 프레임 속도 = 지연시간 이다.
# 일반적인 동영상은 주로 25ms의 프레임 속도를 가진다.
