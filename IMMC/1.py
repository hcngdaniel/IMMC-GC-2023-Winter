#!/usr/bin/env python3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel("dataset.xlsx")
print(df.columns)
cnt = 0
for cls in df.columns[7:8]:
    for i in range(1, 9):
        target = df.loc[df.loc[:, "Species_num"] == i, cls]
        t = plt.hist(target, bins=int(target.max()-target.min()+1), alpha=0.9, label=f"Species {i}")
    cnt += 1
plt.legend()
plt.title("FPNr")
plt.xticks(np.arange(5, 27, 1.))
plt.show()

gain = 11
print((df.loc[df["Species_num"] == 5, cls] <= 11).sum(), (df.loc[df["Species_num"] != 5, cls] <= 11).sum())
print((df.loc[df["Species_num"] == 5, cls] > 11).sum(), (df.loc[df["Species_num"] != 5, cls] > 11).sum())
