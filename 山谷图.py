# -*- coding: utf-8 -*-
# @Author  : zhouxin
# @Time    : 2023/3/5 21:44
# @File    : 山谷图.py
# @annotation    :


with open("data.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    subnetwork_size = lines[0].strip("\n")
    times_stable = lines[1].strip("\n")
    print(subnetwork_size, times_stable)
