# 폰트 관리자 (Font Manager)

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.style.use(["seaborn-notebook"])

fig = plt.figure()
ax = plt.axes

# 사용할 수 있는 폰트 목록
print(set([f.name for f in mpl.font_manager.fontManager.ttflist]))

# 폰트 지정
font1 = {'family': 'DejaVu Sans Mono', 'size':24, 'color':'black'}
font2 = {'family': 'Impact', 'size':18, 'weight':'bold', 'color':'red'}
font3 = {'family': 'MS Gothic', 'size':10, 'weight': 'light', 'color':'blue'}

plt.plot([1,2,3,4,5],[4,1,6,3,2])
# 지정된 폰트 불러오기
plt.title('title', fontdict=font1)
plt.xlabel('xlabel', fontdict=font2)
plt.ylabel('ylabel', fontdict=font3)

plt.show()