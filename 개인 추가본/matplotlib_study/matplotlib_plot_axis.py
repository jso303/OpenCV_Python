# 플롯 축
# x,y 축 범위 지정하기

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.style.use(["seaborn-notebook"])

fig = plt.figure()
ax = plt.axes

# 플롯 x,y 축 범위 지정
plt.plot(np.random.randn(50))
plt.xlim(-1, 50)
plt.ylim(-5, 5)

# 한번에 범위 지정도 가능
fig = plt.figure()
plt.plot(np.random.randn(50))
plt.axis([-1,50,-5,5])

# 범위에 딱 맞게 지정
fig = plt.figure()
plt.plot(np.random.randn(50))
plt.axis('tight')

# 범위를 넉넉하게 지정
fig = plt.figure()
plt.plot(np.random.randn(50))
plt.axis('equal')


plt.show()