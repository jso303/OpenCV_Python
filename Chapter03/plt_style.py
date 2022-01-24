import matplotlib.pyplot as plt
import numpy as np

x = np.arange(10)
f1 = x * 5
f2 = x **2
f3 = x **2 + x*2

plt.plot(x, 'r-')   # x 값  : 빨간 색 이음선
plt.plot(f1, 'g.')  # f1 값 : 녹색 점
plt.plot(f2, 'bv')  # f2 값 : 파란색 역삼각형
plt.plot(f3, 'ks')  # f3 값 : 검은색 사각형
plt.show()