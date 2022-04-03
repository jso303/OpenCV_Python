# 파이 차트
# 원 그래프
# 전체적인 비율을 쉽게 파악 가능

from unicodedata import category
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.style.use(["seaborn-notebook"])

# 파이 그래프 그리기

plt.figure(1)
data = [10, 50, 30, 40, 60]
categories = ['C1', 'C2', 'C3', 'C4', 'C5']
plt.pie(data, labels=categories, autopct="%0.1f%%")
plt.legend(categories)

# 공간 띄워 그리기
plt.figure(2)
data = [10, 50, 30, 40, 60]
explode = [0.1, 0.1, 0.1, 0.1, 0.1]
categories = ['C1', 'C2', 'C3', 'C4', 'C5']
plt.pie(data, explode, labels=categories, autopct="%0.1f%%")
plt.legend(categories)

# 도넛 차트 그리기
plt.figure(3)
data = [10, 50, 30, 40, 60]

categories = ['C1', 'C2', 'C3', 'C4', 'C5']
plt.pie(data, wedgeprops = dict(width=0.5), explode = [0.1, 0.1, 0.1, 0.1, 0.1]
, labels=categories, autopct="%0.1f%%")
plt.legend(categories)


plt.show()