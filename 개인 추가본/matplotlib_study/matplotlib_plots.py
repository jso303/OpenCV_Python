# 플롯

# bar : 막대 플롯(bar plot) 생성
# barbs : barbs의 2차원 필드 그리기
# boxplot : 상자 및 수염 플롯 생성
# cohere : x와 y의 일관성 시각화 그리기
# contour : 플롯 등고선
# errorbar : 오류 막대 그래프
# hexbin : 육각형 binning 플롯 생성
# hist : 히스토그램 플롯
# imshow : 축에 이미지 표시
# pcolor : 2차원 배열의 유사 플롯 생성
# pcolormesh : 사각 망사 그래프
# pie : 파이 차트 플롯
# plot : 플롯 라인 또는 마커
# quiver : 화살표의 2차원 필드 생성
# sankey : Sankey 흐름도 생성
# scatter : x대 y의 산점도 생성
# stem : 줄기 그래프 생성
# streamplot : 백터 흐름의 스트림 라인 그리기

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.style.use(["seaborn-notebook"])

# 막대 플롯 생성하기
plt.figure(1)
height = [np.random.randn() * i for i in range(1,6)]
names = ['A', 'B', 'C', 'D', 'E']
y_pos = np.arange(len(names))
plt.bar(y_pos, height)
plt.xticks(y_pos, names, fontweight='bold')
plt.xlabel('group')

# 가로 막대 플롯 생성하기
plt.figure(2)
height = [np.random.randn() * i for i in range(1,6)]
names = ['A', 'B', 'C', 'D', 'E']
y_pos = np.arange(len(names))
plt.barh(y_pos, height)
plt.yticks(y_pos, names, fontweight='bold')
plt.ylabel('group')


# 스택 막대 플롯 
plt.figure(3)
bars1 = [12, 22, 9, 8, 26]
bars2 = [19, 7, 31, 36, 10]
bars3 = [25, 30, 26, 13, 7]
bars = np.add(bars1, bars2).tolist()

r = [0,1,2,3,4]
names = ['A', 'B', 'C', 'D', 'E']
plt.bar(r, bars1, color='royalblue', edgecolor='white')
plt.bar(r, bars2, bottom=bars1, color='skyblue', edgecolor='white')
plt.bar(r, bars3, bottom=bars2, color='lightblue', edgecolor='white')

plt.xlabel('group', fontweight='bold')
plt.xticks(r, names, fontweight='bold')

# width 스택 막대 플롯
plt.figure(4)

bar_width = 0.25
bars1 = [8, 12, 29, 10, 16]
bars2 = [9, 27, 30, 16, 13]
bars3 = [15, 22, 13, 29, 17]

r1 = np.arange(len(bars1))
r2 = [x + bar_width for x in r1]
r3 = [x + bar_width for x in r2]


names = ['A', 'B', 'C', 'D', 'E']
plt.bar(r1, bars1, color='royalblue', width=bar_width, edgecolor='white', label='r1')
plt.bar(r2, bars2, color='skyblue', width=bar_width, edgecolor='white', label='r2')
plt.bar(r3, bars3, color='lightblue', width=bar_width, edgecolor='white', label='r3')

plt.xlabel('group', fontweight='bold')
plt.xticks([r + bar_width for r in range(len(bars1))], ['A', 'B', 'C', 'D', 'E'])
plt.legend()

plt.show()