# 플롯 레이블
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.style.use(["seaborn-notebook"])

fig = plt.figure()
ax = plt.axes

plt.plot(np.random.randn(50), label = 'A')
plt.plot(np.random.randn(50), label = 'B')
plt.plot(np.random.randn(50), label = 'C')
plt.title("tilte")
plt.xlabel("x")
plt.ylabel("random.randn")

# 라벨(범례) 표시
plt.legend()

plt.show()