# -*- coding: utf-8 -*-
# @Author  : zhouxin
# @Time    : 2023/3/4 10:07
# @File    : 8.4.py
# @annotation    :


import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-2 * np.pi, -2 * np.pi)
y = np.sin(x)
y1 = np.cos(x)

ax = plt.subplot(111)
ax.plot(x, y, ls="-", lw=2, label="$\sin(x)$")
ax.plot(x, y1, ls="-", lw=2, label="$\cos(x)$")
ax.legend(loc="lower left")
plt.title("$\sin(x)$" + "和" + "$\cos(x)$" + "函数")

plt.xticks(
    [-2 * np.pi, -3 * np.pi / 2, -1 * np.pi, -1 * np.pi / 2, 0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi],
    [
        "$-2 * np.pi$",
        "$-3 * np.pi / 2$",
        "$-1 * np.pi$",
        "$-1 * np.pi / 2$",
        "$0$",
        "$np.pi / 2$",
        "$np.pi$",
        "$3 * np.pi / 2$",
        "$2 * np.pi$",
    ],
)

ax.spines["right"].set_color("none")

ax.spines["top"].set_color("none")

ax.spines["bottom"].set_position(("data", 0))
ax.spines["left"].set_position(("data", 0))

ax.xaxis.set_ticks_position("bottom")
ax.yaxis.set_ticks_position("left")
plt.show()
