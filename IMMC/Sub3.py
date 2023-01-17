#!/usr/bin/env python3
import numpy as np
import math
import pandas as pd


df = pd.read_excel("dataset.xlsx")

mean = [df[df["Species_num"] == i].iloc[:, 3:].mean() for i in range(1, 9)]
std = [df[df["Species_num"] == i].iloc[:, 3:].std() for i in range(1, 9)]
sex_mean = [[df[[k[0] and k[1] for k in zip(df["Sex_num"] == j, df["Species_num"] == i)]].iloc[:, 3:].mean() for j in range(1, 3)] for i in range(1, 9)]
sex_std = [[df[[k[0] and k[1] for k in zip(df["Sex_num"] == j, df["Species_num"] == i)]].iloc[:, 3:].std() for j in range(1, 3)] for i in range(1, 9)]


def gaussian():

