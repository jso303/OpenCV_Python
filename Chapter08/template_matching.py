# 템플릿 매칭으로 객체 위치 검출
# 템플릿 매칭은 크기, 방향, 회전 등의 변화에는 약하고 속도가 느린 단점이 있다

# 찾을 물체가 있는 영상을 준비해 두고 그 물체가 포함되어 있을 것이라 예상되는
# 입력 영상과 비교해서 물체가 매칭되는 위치를 찾는다.
# 미리 준비해둔 미리 찾을 물체 영상을 템플릿 영상이라고 함

# 템플릿 영상은 입력 영상보다 항상 크기가 작아야 한다.


import cv2
import numpy as np

# 입력 영상
img = cv2.imread("./img/figures.jpg")
# 템플릿 영상
template = cv2.imread("./img/taekwonv1.jpg")
th, tw = template.shape[:2]
cv2.imshow("template", template)

# 세 가지 매칭 메서드 순회

# 매칭 메서드 종류 9개 중 현재 사용중인 매칭 3가지
# cv2.TM_CCOEFF_NORMED : 상관계수 매칭의 정규화,    완벽 매칭 = 1, 나쁜 매칭 = -1
# cv2.TM_CCORR_NORMED : 상관관계 매칭의 정규화,     완벽 매칭 = 큰 값, 나쁜 매칭 = 0
# cv2.TM_SQDIFF_NORMED : 제곱 차이 매칭의 정규화,   완벽 매칭 = 0, 나쁜 매칭 = 큰 값
methods = ["cv2.TM_CCOEFF_NORMED", "cv2.TM_CCORR_NORMED", "cv2.TM_SQDIFF_NORMED"]


for i, method_name in enumerate(methods):
    img_draw = img.copy()
    method = eval(method_name)
    # 템플릿 매칭
    # cv2.matchTemplate(입력영상, 템플릿 영상, 매칭 메서드)
    res = cv2.matchTemplate(img, template, method)
    # 최대, 최소 값과 그 좌표 구하기
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    print(method_name, min_val, max_val, min_loc, max_loc)
    
    # cv2.TM_SQDIFF 의 경우 최소 값이 좋은 매칭, 나머지는 반대
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
        match_val = min_val
        
    else:
        top_left = max_loc
        match_val = max_val
        
    # 매칭 좌표를 구해서 빨간색 사각형으로 표시
    bottom_right = (top_left[0] + tw, top_left[1] + th)
    cv2.rectangle(img_draw, top_left, bottom_right, (0,0,255), 2)
    # 매칭 값 표시
    cv2.putText(img_draw, str(match_val), top_left, cv2.FONT_HERSHEY_PLAIN,\
                2, (0,255,0), 1, cv2.LINE_AA)
    cv2.imshow(method_name, img_draw)
cv2.waitKey(0)
cv2.destroyAllWindows()