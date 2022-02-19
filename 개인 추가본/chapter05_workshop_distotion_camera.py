# 챕터 5장에서의 카메라 조정도 resize와 flip로 해결이 가능

# 왜곡 거울 카메라

# 렌즈 왜곡을 사용하여 하나의 영상에 원본, 좌우 거울 왜곡, 상하 거울 왜곡, 물결 왜곡,
# 볼록 렌즈 왜곡, 오목 렌즈 왜곡 효과를 하나의 영상에 병합해 출력

# 각각의 왜곡 효과를 위한 리매핑 좌표는 매번 구할 필요 없이 한번 만들어진 리매핑 좌표에
# 새로운 프레임을 리매핑 하면 됨

import cv2
import numpy as np

# 내장 카메라 사용
# 크기 320x240
cap = cv2.VideoCapture(0)

rows, cols = 480, 640
map_y, map_x = np.indices((rows, cols), dtype=np.float32)   # 기본 매핑 좌표

# 거울 왜곡 효과
map_mirrorh_x, map_mirrorh_y = map_x.copy(), map_y.copy()
map_mirrorv_x, map_mirrorv_y = map_x.copy(), map_y.copy()
# 좌우 대칭 좌표 연산
map_mirrorh_x[:, cols//2:] = cols - map_mirrorh_x[:, cols//2:] -1
# 상하 대칭 좌표 연산
map_mirrorv_y[rows//2:, :] = rows - map_mirrorv_y[rows//2:, :] -1


# 물결 효과 (sin)
map_wave_x, map_wave_y = map_x.copy(), map_y.copy()
map_wave_x = map_wave_x + 15*np.sin(map_y/20)
map_wave_y = map_wave_y + 15*np.sin(map_x/20)


# 렌즈 효과
# 중심점 좌상단에서 중앙으로 변경
map_lenz_x = 2*map_x/(cols -1) -1
map_lenz_y = 2*map_y/(rows -1) -1

# 극좌표 변환
r, theta = cv2.cartToPolar(map_lenz_x, map_lenz_y)
r_convex = r.copy()
r_concave = r

# 볼록 렌즈 효과 매핑 좌표 연산
r_convex[r<1] = r_convex[r<1] **2
print(r.shape, r_convex[r<1].shape)

# 오목 렌즈 효과 매핑 좌표 연산
r_concave[r<1] = r_concave[r<1] **0.5

# 렌즈 효과 극 좌표 -> 직교 좌표로 복원
map_convex_x, map_convex_y = cv2.polarToCart(r_convex, theta)
map_concave_x, map_concave_y = cv2.polarToCart(r_concave, theta)

# 렌즈 효과 중앙 좌표 -> 좌상단 좌표 복원
map_convex_x = ((map_convex_x +1) *cols -1)/2
map_convex_y = ((map_convex_y +1) *rows -1)/2
map_concave_x = ((map_concave_x +1)*cols -1)/2
map_concave_y = ((map_concave_y +1)*rows -1)/2

while True:
    ret, frame = cap.read()
    filp_frame = cv2.flip(frame, 1)

    
    # 준비된 매핑 좌표로 영상 효과 적용
    mirrorh=cv2.remap(filp_frame, map_mirrorh_x, map_mirrorh_y, cv2.INTER_LINEAR)
    mirrorv=cv2.remap(filp_frame, map_mirrorv_x, map_mirrorv_y, cv2.INTER_LINEAR)
    wave = cv2.remap(filp_frame, map_wave_x, map_wave_y, cv2.INTER_LINEAR, None,\
                     cv2.BORDER_REPLICATE)
    convex = cv2.remap(filp_frame, map_convex_x, map_convex_y, cv2.INTER_LINEAR)
    concave = cv2.remap(filp_frame, map_concave_x, map_concave_y, cv2.INTER_LINEAR)
    
    # resize_frame = cv2.resize(filp_frame, dsize=(320,240), interpolation=cv2.INTER_LINEAR)
    
    # 영상 합치기
    r1 = np.hstack((filp_frame, mirrorh, mirrorv))
    r2 = np.hstack((wave, convex, concave))
    merged = np.vstack((r1,r2))
    
    resize_frame = cv2.resize(merged, None, fx=0.7, fy=0.7, interpolation=cv2.INTER_LINEAR)
    cv2.imshow("distorted", resize_frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()    
    