# -*- coding: utf-8 -*-
# @Author  : zhouxin
# @Time    : 2023/3/5 21:36
# @File    : 三维图.py
# @annotation    :

from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np

ax = plt.axes(projection='3d')

# 三维线的数据
zline = np.linspace(0, 15, 1000)
xline = np.sin(zline)
yline = np.cos(zline)
ax.plot3D(xline, yline, zline, 'gray')

# 三维散点的数据
zdata = 15 * np.random.random(100)
xdata = np.sin(zdata) + 0.1 * np.random.randn(100)
ydata = np.cos(zdata) + 0.1 * np.random.randn(100)
ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Greens');

plt.show()
