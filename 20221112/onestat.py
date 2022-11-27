import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

nsample = 20
x = np.linspace(0, 10, nsample)
X = sm.add_constant(x)
bata = np.array([2, 5])
e = np.random.normal(size=nsample)
y = np.dot(X, bata) + e
model = sm.OLS(y, X)  # 最小二乘法
results = model.fit()  # 拟合
results.params  # 拟合参数
results.summary()  # 拟合结果
y_ = results.fittedvalues  # 拟合值

fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(x, y, 'o', label="data")  # 原始数据
ax.plot(x, y_, 'r--.', label="test")  # 拟合数据
ax.legend(loc='best')
plt.show()
