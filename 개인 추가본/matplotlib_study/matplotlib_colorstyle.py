# 색상 스타일 (Color Style)

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.style.use(["seaborn-notebook"])

fig = plt.figure()
ax = plt.axes

# 색상 지정 
plt.plot(np.random.randn(50).cumsum(), color='g')
plt.plot(np.random.randn(50).cumsum(), color='b')
# 색상 코드 값
plt.plot(np.random.randn(50).cumsum(), color='#1243FF')
# 색상 RGB 실수 표현
plt.plot(np.random.randn(50).cumsum(), color=(0.2,0.4,0.6))
# 색상 이름 값
plt.plot(np.random.randn(50).cumsum(), color='navy')


# 라인 스타일과 색상 스타일 같이 지정가능
fig = plt.figure()
plt.plot(np.random.randn(50).cumsum(), 'c-')
plt.plot(np.random.randn(50).cumsum(), 'm-.')
plt.plot(np.random.randn(50).cumsum(), 'r:')

plt.show()
