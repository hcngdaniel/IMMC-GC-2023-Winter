#!/usr/bin/env python3
import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd
import torch


df = pd.read_excel("dataset.xlsx")
mean = [df[df["Species_num"] == i].iloc[:, 3:].mean() for i in range(1, 9)]
std = [df[df["Species_num"] == i].iloc[:, 3:].std() for i in range(1, 9)]
density = df["Species_num"].value_counts() / df["Species_num"].value_counts().sum()

def gaussian(n, m, x):
    return 1 / (std[n][m] * (2 * math.pi) ** 0.5) * math.exp(-(x - mean[n][m]) ** 2 / (2 * std[n][m] ** 2))


correct = 0
wrong = 0

table = torch.zeros((8, 2))

conditions = []

class1 = 0
class2 = 4

for i in range(0, 100):
    for j in range(0, 100):
        prob = [0 for k in range(9)]
        for n in range(1, 9):
            prod = density[n]
            prod *= gaussian(n - 1, class1, i)
            prod *= gaussian(n - 1, class2, j)
            prob[n] = prod
        if max(prob) == prob[5]:
            conditions.append([i, j])
#
# plt.scatter([conditions[i][0] for i in range(len(conditions))], [conditions[i][1] for i in range(len(conditions))])
# plt.show()
a, b, c, d = 0, 0, 0, 0
for i in range(len(df)):
    is5 = False
    if [df.iloc[i, 3 + class1], df.iloc[i, 3 + class2]] in conditions:
        is5 = True
    if is5 and df.loc[i, "Species_num"] == 5:
        a += 1
    if is5 and df.loc[i, "Species_num"] != 5:
        b += 1
    if (not is5) and df.loc[i, "Species_num"] == 5:
        c += 1
    if (not is5) and df.loc[i, "Species_num"] != 5:
        d += 1
print(a, b)
print(c, d)
