import numpy as np

# 定义数据x：温度，y：反应速率
x = [298.1, 300.1, 400.1, 500.1, 600.1]
x = np.array(x)
y = [2.6e-35, 3.25e-35, 1.42e-31, 2.51e-29, 8.69e-28]
y = np.array(y)
x_1 = 373.15  # 100°C

f1 = np.polyfit(x, y, 3)  # 用3次多项式拟合
f2 = np.poly1d(f1)  # 得到函数
y_1 = f2(x_1)

print('100°C下的反应速率为\n', y_1)
