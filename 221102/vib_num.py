import numpy as np

a = np.loadtxt('6.txt', skiprows=3, usecols=1, comments='"', encoding='utf-8')
x = 0  # 记录原子数
y = 0  # 记录振动数
for i in range(len(a)):
    if a[i] == 0:
        x = x + 1
    elif a[i] > 0:
        y = y + 1
x = x - 1
if x == 1:
    print('此为单原子')
elif y == 3 * x - 5:
    print('此为线性分子')
elif y == 3 * x - 6:
    print('此为非线性分子')
