import numpy as np

a = np.loadtxt('7.txt', skiprows=2, usecols=(1, 2, 3), encoding='utf-8')
d = np.sqrt((a[0][0] - a[1][0]) ** 2 + (a[0][1] - a[1][1]) ** 2 + (a[0][2] - a[1][2]) ** 2)
print('距离为\n', d)
