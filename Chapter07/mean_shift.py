# 평균 이동 세그멘테이션 필터

import cv2
import numpy as np

img = cv2.imread("./img/taekwonv1.jpg")
def onChange(x):
    sp = cv2.getTrackbarPos("sp", "img")    # 평균을 낼 픽셀 크기
    sr = cv2.getTrackbarPos("sr", "img")    # 색상 값의 차이 범위
    lv = cv2.getTrackbarPos("lv", "img")    # 이미지 크기 변환(높은 단계에서 속도 증가, 해상도 감소)
    
    # cv2.pyrMeanShiftFiltering(입력 영상, 공간 윈도 반지름 크기, 색상 윈도 반지름 크기,\
    #                           결과 영상, 이미지 피라미드 최대 레벨)
    mean = cv2.pyrMeanShiftFiltering(img, sp, sr, None, lv)
    cv2.imshow("img",  np.hstack((img,mean)))
    
cv2.imshow("img", np.hstack((img, img)))
# 수치 조정 트랙바
cv2.createTrackbar("sp", "img", 0,100, onChange)
cv2.createTrackbar("sr", "img", 0,100, onChange)
cv2.createTrackbar("lv", "img", 0,5, onChange)
cv2.waitKey(0)
cv2.destroyAllWindows()