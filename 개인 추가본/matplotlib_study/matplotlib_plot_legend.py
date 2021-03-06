# 플롯 범례
# 0 : best
# 1 : upper right
# 2 : upper left
# 3 : lower left
# 4 : lower right
# 5 : right
# 6 : center left
# 7 : center right
# 8 : lower center
# 9 : upper center


from cv2 import line
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.style.use(["seaborn-notebook"])

fig, ax = plt.subplots()

ax.plot(np.random.randn(10), '-r', label='A')
ax.plot(np.random.randn(10), ':g', label='B')
ax.plot(np.random.randn(10), '--b', label='C')
ax.axis('equal')

# 기본은 best 위치
# ax.legend()

# 위의 중앙, 범례 박스 제거, 범례 col 2개로 설정
ax.legend(loc='upper center', frameon=False, ncol = 2)

# 그림자, 여백 추가
ax.legend(fancybox=True, framealpha = 1, shadow=True, borderpad=1)

plt.figure(figsize=(8,4))
x = np.linspace(0, 10, 1000)
y = np.cos(x[:, np.newaxis] * np.arange(0, 2, 0.2))
lines = plt.plot(x,y)
plt.legend(lines[:3], ['c1', 'c2', 'c3'], loc='upper right')

plt.figure()
plt.plot(x, y[:, 0], label='c1')
plt.plot(x, y[:, 1], label='c2')
plt.plot(x, y[:, 2], label='c3')
plt.plot(x, y[:, 3])
plt.legend(framealpha=1, frameon=True)


plt.show()
