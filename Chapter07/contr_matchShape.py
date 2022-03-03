# 도형 매칭으로 비슷한 도형 찾기

import cv2
import numpy as np

target = cv2.imread("./img/4star.jpg")
shapes = cv2.imread("./img/shapestomatch.jpg")

targetGray = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)
shapesGray = cv2.cvtColor(shapes, cv2.COLOR_BGR2GRAY)

ret, targetTh = cv2.threshold(targetGray, 127, 255, cv2.THRESH_BINARY_INV)
ret, shapesTh = cv2.threshold(shapesGray, 127, 255, cv2.THRESH_BINARY_INV)

# 컨투어 찾기
cntrs_target, _ = cv2.findContours(targetTh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cntrs_shapes, _ = cv2.findContours(shapesTh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

matchs = []
for contr in cntrs_shapes:
    # 도형매칭 함수
    # cv2.matchShapes(비교할 컨투어 1, 비교할 컨투어 2, 비교 알고리즘 선택 플래그, 알고리즘의 전달을 위한 예비 인수, 닮음 정도(0으로 갈 수록 동일))
    # 대상 도형과 여러 도형 중 하나와 매칭 실행 (반복문으로 도형 1, 2, 3 과 순서대로 비교)
    match = cv2.matchShapes(cntrs_target[0], contr, cv2.CONTOURS_MATCH_I2, 0.0)
    # 매칭 점수와 컨투어를 쌍으로 저장
    matchs.append((match, contr))
    # 해당 컨투어의 시작 위치에 매칭 점수 표시
    cv2.putText(shapes, "%.2F"%match, tuple(contr[0][0]), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 1)

matchs.sort(key=lambda x : x[0])

# 가장 적은 매칭 점수를 얻는 도형에 컨투어 그리기(녹색)
cv2.drawContours(shapes, [matchs[0][1]], -1, (0,255,0), 3)
cv2.imshow("target", target)
cv2.imshow("Match Shape", shapes)
cv2.waitKey()
cv2.destroyAllWindows()