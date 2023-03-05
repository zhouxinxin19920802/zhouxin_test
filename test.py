# -*- coding: utf-8 -*-
# @Author  : zhouxin
# @Time    : 2023/3/4 16:46
# @File    : test.py
# @annotation    :


import numpy as np
import matplotlib.pyplot as plt


x = np.arange(0.00001, 100, 0.0001)
y = 1 / x + x + x**2

max_value = float("inf")


id = 0
for item in x:
    y_value = 1 / item + item + item**2
    if y_value < max_value:
        id = item
        max_value = y_value

print("id:", id, " ", "y_value:", max_value)
print(min(y))
plt.plot(x, y)
plt.show()
plt.save("1.png")