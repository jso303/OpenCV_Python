# 라인 플롯(Line Plot)
# 플롯은 그림(figure)와 축(axes)로 구성
# plt.figure : 축과 그래픽, 텍스트, 레이블을 표시하는 모든 객체를 포함하는 컨테이너
# plt.axes : 눈금과 레이블이 있는 테두리 박스로 시각화를 형성하는 플롯 요소 포함

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.style.use(["seaborn-notebook"])
# 기본 x,y 축 크기 (0.0~1.0)

# 대각 직선 그리기
fig = plt.figure()
ax = plt.axes
plt.plot([0,0.2,0.4,0.6,0.8,1.0])

# sin, cos 함수 그리기
fig = plt.figure()
x = np.arange(0, 10, 0.01)
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))

# 랜덤 함수 그리기
fig = plt.figure()
plt.plot(np.random.randn(50))

plt.show()

