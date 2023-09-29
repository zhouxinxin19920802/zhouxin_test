# coding: utf-8


import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["SimHei"]  # 设置字体
plt.rcParams["axes.unicode_minus"] = False  # 该语句解决图像中的“-”负号的乱码问题

game = [0, 2, 4, 6, 8, 10]
scores = [16, 16, 4, 6, 9, 9]
plt.plot(game, scores, ls="-", c="black", marker="d")

plt.xticks(game, ["t0", "t1", "t2", "t3", "t4", "t5"])


plt.xlabel("时间", fontdict={"size": 12})
plt.ylabel("指挥链数量", fontdict={"size": 12})

plt.legend(loc="upper right", title="杀伤链数量")
plt.show()
