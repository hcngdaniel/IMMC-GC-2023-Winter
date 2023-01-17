#!/usr/bin/env python3
import torch
import numpy as np
import pandas as pd
import math


df = pd.read_excel("dataset.xlsx")

density = df["Species_num"].value_counts() / df["Species_num"].value_counts().sum()
mean = [df[df["Species_num"] == i].iloc[:, 3:].mean() for i in range(1, 8 + 1)]
std = [df[df["Species_num"] == i].iloc[:, 3:].std() for i in range(1, 8 + 1)]


def gaussian(n, m, x):
    return 1 / (std[n][m] * (2 * math.pi) ** 0.5) * np.exp(-(x - mean[n][m]) ** 2 / (2 * std[n][m] ** 2))


def mixture(m, x):
    p = 0
    for i in range(8):
        p += gaussian(i, m, x) * density[i + 1]
    return p


poss_mat = torch.zeros((len(df), 8, 23), dtype=torch.float32)
label = torch.zeros((len(df), 8), dtype=torch.float32)
for i in range(len(df)):
    for n in range(8):
        for m in range(23):
            poss_mat[i][n][m] = gaussian(n, m, df.iloc[i, 3 + m]) * density[n + 1] / mixture(m, df.iloc[i, 3 + m])
    label[i][df["Species_num"][i] - 1] = 1
# torch.save(poss_mat, "dataset.pth")
# torch.save(label, "label.pth")
