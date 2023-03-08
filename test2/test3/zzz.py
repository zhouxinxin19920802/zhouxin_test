# -*- coding: utf-8 -*-
# @Author  : zhouxin
# @Time    : 2023/3/6 19:06
# @File    : zzz.py
# @annotation    :


from ffff1 import Employee1

import matplotlib.pyplot as plt
from scipy.signal import savgol_filter as sg
def data_read(shape_data, data):
    data_shape_after = []
    for line in open(shape_data, "r", encoding="utf-8"):
        line = line.strip("\n")
        data_shape_after.append(float(line))
    with open(data, "r", encoding="utf-8") as f:
        lines = f.readlines()
        times_stable = int(float(lines[0].strip("\n")))
    times_start = 450
    data_resilience = data_shape_after[times_start: times_stable + 100]
    data_resilience_sg = sg(data_resilience, window_length=25, polyorder=1)