파이썬으로 만드는 OpenCV 프로젝트
==========================

## 스터디 개요

- 스터디 목적은 졸업과제를 위한 OpenCV 기술 습득입니다.
- '파이썬으로 만드는 OpenCV 프로젝트(이세우 저)' 교재를 활용하여 스터디를 했습니다.

## 스터디 일지

- 2022.01.09
  - [파이썬으로 만드는 OpenCV 프로젝트] 책 구매

- 2022.01.10
  - 1장: 개요와 설치 (p.1~21)
  - 
- 2022.01.11~01.14
  - 2장: 기본 입출력 (p.23-59)

- 2022.01.16~01.19
  - 3장: Numpy와 Matplotlib (p.61-104)

- 2022.01.21~02.04
  - 4장: 이미지 프로세싱 기초 (p.105-174)
  - 예제에 사용되는 이미지를 구글에서 개인적으로 구해 예제를 작성하였으나 이후 구하기 힘든 이미지가 있어 책에서 지원하는 이미지 사용 시작.
  - 3장까지 사용된 예제는 업로드된 이미지와 다르므로 오류가 있을 수 있음

- 2022.02.04~02.09
  - 5장: 기하학적 변환 (p.175-213)
  - workshop_distotion_camera.py 에서 캠 크기 조절이 안되어 3개로 나누어 출력하는 방식으로 변환함

- 2022.02.10~02.19
  - 6장: 영상 필터 (p.215-250)

- 2022.02.19~03.04
  - 7장: 영상 분할 (p.251-300)
  - 예제 7-10에 사용할 동전 이미지가 없어 구글에서 사용, 원 사이 거리와 스레시 홀드 값을 조정하여 이미지에 맞게 처리

- 2022
  - 8장: 영상 매칭과 추적 (p.301~376)
  - 
- 2022
  - 9장: 머신러닝 (p.377~p.446)


## 개인 추가본 폴더

- 책의 코드가 현재 버전과 호환되지 않거나 이외의 문제로 해결 못한 부분을 이후에 수정, 정리.

- 2022.02.19
  - 2장 예제 2-7, 5장 실전 워크숍 예제 5-17에서 웹캠 좌우반전 상태 출력, 크기 조정 문제
  - 기본 출력이 좌우 반전 상태이므로 cv2.filp로 좌우반전을 해주고 웹캠 크기는 set이 아닌 cv2.resize를 이용해 해결
  - set은 웹캠에서 자체 지원하는 크기로만 조정가능, resize는 자유롭게 조정 가능

- 2022.02.25
  - 5장 예제 5-8에서 스캔이 안되던 문제
  - 폭과 너비의 타입이 맞지 않아서 안됨. int를 씌워 해결


## 이미지 파일 다운로드

이미지 파일은 [이곳](https://github.com/dltpdn/insightbook.opencv_project_python)에서 다운받으시면 됩니다.
