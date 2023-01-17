#!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("dataset.xlsx")

classes = df.columns.values[3:]
classes = classes[13:]
print(classes)
space = 1
figure, axis = plt.subplots(4, 4)
cnt = 0
for cls in classes:
    for i in range(1, 3):
        target = df.loc[df.loc[:, "Sex_num"] == i, cls]
        if cls == "aNDSr":
            space = 0.1
        print(cnt // 4, cnt % 4)
        axis[cnt // 4][cnt % 4].hist(target, bins=int((target.max()-target.min())), density=True, alpha=0.5)
    axis[cnt // 4][cnt % 4].set_title(cls)
    cnt += 1
plt.show()