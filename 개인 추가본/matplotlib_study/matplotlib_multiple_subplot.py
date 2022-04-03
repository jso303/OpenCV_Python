# 다중 플롯

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.style.use(["seaborn-notebook"])

ax1 = plt.axes()
ax2 = plt.axes([0.65, 0.5, 0.2, 0.3])

fig = plt.figure()
# 여백 0.4, 0.4를 줌
fig.subplots_adjust(hspace=0.4, wspace=0.4)
for i in range(1,10):
    plt.subplot(3,3,i)
    plt.text(0.5, 0.5, str((3,3,i)), ha='center')

# subplots를 이용해서 한번에 다중 플롯 생성
fig, ax = plt.subplots(3,3, sharex='col', sharey='row')


# 규격 결합으로 크기 설정
fig = plt.figure()
grid = plt.GridSpec(2,3, hspace=0.4, wspace=0.4)

# 0,0
plt.subplot(grid[0,0])
# 0, 1~2
plt.subplot(grid[0,1:])
# 1, 0~1
plt.subplot(grid[1,:2])
# 1, 2
plt.subplot(grid[1,2])


plt.figure(figsize=(5,6))
x = range(1,21)
columns = [np.random.randn(20) * i for i in range(1,7)]
    
i = 0
for c in columns:
    i += 1
        
    plt.subplot(3,2,i)
    plt.plot(x, c, marker='o', linewidth=1, label=c)
    plt.xlim(-1,21)
    plt.ylim(c.min()-1, c.max()+1)


plt.show()

