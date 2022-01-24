import matplotlib.pyplot as plt
import numpy as np

x = np.arange(10)

plt.subplot(2,2,1)      # 2행2열의 1번
plt.plot(x,x**2)        # x의 제곱

plt.subplot(2,2,2)      # 2행2열의 2번
plt.plot(x,x*5)         # x의 5배

plt.subplot(223)        # 2행2열의 3번
plt.plot(x, np.sin(x))  # sin(x)

plt.subplot(224)        # 2행2열의 4번
plt.plot(x, np.cos(x))  # cos(x) 

plt.show()