# 라인 스타일 (Line Style)
# '-' : 'solid'     (선)
# '--' : 'dashed'   (점선)
# '-.' : 'dashdot'  (선, 점선 혼합)
# ':' : 'dotted'    (점선)

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.style.use(["seaborn-notebook"])

fig = plt.figure()
ax = plt.axes

# 랜덤값 누적합
# plt.plot(np.random.randn(50).cumsum(), linestyle='solid')
# plt.plot(np.random.randn(50).cumsum(), linestyle='dashed')
# plt.plot(np.random.randn(50).cumsum(), linestyle='dashdot')
# plt.plot(np.random.randn(50).cumsum(), linestyle='dotted')

plt.plot(np.random.randn(50).cumsum(), linestyle='-')
plt.plot(np.random.randn(50).cumsum(), linestyle='--')
plt.plot(np.random.randn(50).cumsum(), linestyle='-.')
plt.plot(np.random.randn(50).cumsum(), linestyle=':')

plt.show()
