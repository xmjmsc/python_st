import numpy as np

a = [[0 for j in range(5)] for j in range(72)]  # 初始化表
f = open("8.txt", 'r', encoding='utf-8')
i = 1  # 记录原始数据行数
j = 0  # 数组a的行数
for line in f.readlines():
    if i not in (1, 2, 3, 22, 41, 60, 79):  # 这些行的数据不读取
        a[j] = line.split()
        j = j + 1
    i = i + 1
f.close()

b = [[0 for i in range(18)] for i in range(18)]  # 初始化表
for i in range(18):  # 将数组a的数据存入18行18列的数组b中
    for j in range(5):
        b[i][j] = float(a[i][j + 1])
for i in range(18, 36):
    for j in range(5):
        b[i - 18][j + 5] = float(a[i][j + 1])
for i in range(36, 54):
    for j in range(5):
        b[i - 36][j + 10] = float(a[i][j + 1])
for i in range(54, 72):
    for j in range(3):
        b[i - 54][j + 15] = float(a[i][j + 1])
# print(b)
m = 0  # 记录正特征值
n = 0  # 记录负特征值
(x, y) = np.linalg.eig(b)  # 计算特征值
for k in x:
    if k > 0:
        m = m + 1
    elif k < 0:
        n = n + 1
if m == len(x):
    print("此为能量极小值")
elif m == len(x) - 1 and n == 1:
    print("此为过渡态")
else:
    print("此为其他")
