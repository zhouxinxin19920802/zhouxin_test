# coding: utf-8
import math
import os

import matplotlib.pyplot as plt
import numpy
from scipy.signal import savgol_filter as sg


#  参数读取
def data_read(shape_data, data):
    data_shape_after = []
    for line in open(shape_data, "r", encoding="utf-8"):
        line = line.strip("\n")
        data_shape_after.append(float(line))

    times_stable = 0
    with open(data, "r", encoding="utf-8") as f:
        lines = f.readlines()
        times_stable = int(float(lines[0].strip("\n")))
    times_start = 450
    data_resilience = data_shape_after[times_start: times_stable + 100]
    data_resilience_sg = sg(data_resilience, window_length=25, polyorder=1)
    return data_resilience, data_resilience_sg


data_resilience20, data_resilience_sg20 = data_read(
    "./仿真数据/不同尺寸下的数据/60%/20/shape_data.txt", "./仿真数据/不同尺寸下的数据/60%/20" "/data.txt"
)
data_resilience50, data_resilience_sg50 = data_read(
    "./仿真数据/不同尺寸下的数据/60%/50/shape_data.txt", "./仿真数据/不同尺寸下的数据/60%/50" "/data.txt"
)
data_resilience100, data_resilience_sg100 = data_read(
    "./仿真数据/不同尺寸下的数据/60%/100/shape_data.txt", "./仿真数据/不同尺寸下的数据/60%/100" "/data.txt"
)
data_resilience200, data_resilience_sg200 = data_read(
    "./仿真数据/不同尺寸下的数据/60%/200/shape_data.txt", "./仿真数据/不同尺寸下的数据/60%/200" "/data.txt"
)


# plt.plot(data_resilience, label='raw')

plt.plot(
    data_resilience_sg20, color="red", ls="--", lw=1, label="swarm size =20", marker="*"
)
plt.plot(
    data_resilience_sg50,
    color="blue",
    ls="--",
    lw=1,
    label="swarm size =50",
    marker="o",
)
plt.plot(
    data_resilience_sg100,
    color="gold",
    ls="--",
    lw=1,
    label="swarm size =100",
    marker=".",
)
plt.plot(
    data_resilience_sg200,
    color="green",
    ls="--",
    lw=1,
    label="swarm size =200",
    marker="x",
)
plt.legend(loc="upper right")
plt.xlabel("steps")
plt.ylabel("velocity")

plt.show()
