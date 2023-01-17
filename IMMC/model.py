#!/usr/bin/env python3
import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd
import torch


df = pd.read_excel("dataset.xlsx")
mean = [df[df["Species_num"] == i].iloc[:, 3:].mean() for i in range(1, 3)]
std = [df[df["Sex_num"] == i].iloc[:, 3:].std() for i in range(1, 3)]
density = df["Sex_num"].value_counts() / df["Sex_num"].value_counts().sum()

print(mean[0][0])

def gaussian(n, m, x):
    return 1 / (std[n][m] * (2 * math.pi) ** 0.5) * math.exp(-(x - mean[n][m]) ** 2 / (2 * std[n][m] ** 2))


correct = 0
wrong = 0

table = torch.zeros((2, 2))

for i in range(len(df)):
    prob = torch.zeros(3)
    for n in range(1, 3):
        prod = density[n]
        for m in range(3, 26):
            prod *= gaussian(n - 1, m - 3, df.iloc[i][m])
        prob[n] = prod
    if torch.argmax(prob) == df["Sex_num"][i]:
        correct += 1
        table[df["Sex_num"][i] - 1][0] += 1
    else:
        wrong += 1
        table[df["Sex_num"][i] - 1][1] += 1

print(correct, wrong)
print(correct / (correct + wrong), wrong / (correct + wrong))
print(table)
for i in range(2):
    table[i][0], table[i][1] = table[i][0] / (table[i][0] + table[i][1]), table[i][1] / (table[i][0] + table[i][1])
print(table)
