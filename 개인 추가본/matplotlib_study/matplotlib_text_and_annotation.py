# 텍스트와 주석

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.style.use(["seaborn-notebook"])

fig, ax = plt.subplots()
ax.axis([0,10,0,10])

# 데이터값 기준
ax.text(3,6, ". transData(3,6)", transform=ax.transData)
# 축 기준 (0~1.0)
ax.text(0.2, 0.4, ". transAxes(0.2, 0.4)", transform=ax.transAxes)
# 창 크기 기준
ax.text(0.2, 0.2, ".transFigure(0.2, 0.2", transform=fig.transFigure)

# 축 범위 값 변경 (축 기준 좌표만 달라짐)
ax.set_xlim(-6, 10)
ax.set_ylim(-6, 10)

x = np.arange(1, 40)
y = x * 1.1
plt.scatter(x,y, marker='.')
plt.axis('equal')
plt.annotate('point', xy=(4,5), xytext=(20,10), arrowprops=dict(shrink=0.05))

plt.show()