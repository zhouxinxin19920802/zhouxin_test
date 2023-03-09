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
    return data_shape_after