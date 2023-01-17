#!/usr/bin/env python3
import numpy as np
import math
import pandas as pd


df = pd.read_excel("dataset.xlsx")


species_mean = [df[df["Species_num"] == i + 1].iloc[:, 3:].mean() for i in range(8)]
species_std = [df[df["Species_num"] == i + 1].iloc[:, 3:].std() for i in range(8)]
species_density = df["Species_num"].value_counts(normalize=True)

gender_mean = [df[df["Sex_num"] == i + 1].iloc[:, 3:].mean() for i in range(3)]
gender_std = [df[df["Sex_num"] == i + 1].iloc[:, 3:].std() for i in range(3)]
gender_density = df["Sex_num"].value_counts(normalize=True)


def gaussian(mean, std, x):
    if math.isnan(mean) or math.isnan(std):
        return 0
    return 1 / (std * (2 * math.pi) ** 0.5) * math.exp(-(x - mean) ** 2 / (2 * std ** 2))


def classifier2(feat):
    prob = [species_density[i] for i in range(1, 9)]
    for i in range(8):
        for j in range(23):
            prob[i] *= gaussian(species_mean[i][j], species_std[i][j], feat[j])
    prob /= sum(prob)
    return np.argmax(prob)


def classifier3(feat):
    prob = [gender_density[i] for i in range(1, 3)]
    for i in range(2):
        for j in range(23):
            prob[i] *= gaussian(gender_mean[i][j], gender_std[i][j], feat[j])
    prob /= sum(prob)
    return np.argmax(prob)


correct_species = 0
wrong_species = 0
correct_gender = 0
wrong_gender = 0
correct = 0
wrong = 0

for i in range(len(df)):
    feat = df.iloc[i, 3:]
    species = classifier2(feat)
    gender = classifier3(feat)
    if species + 1 == df["Species_num"][i]:
        correct_species += 1
    else:
        wrong_species += 1
    if gender + 1 == df["Sex_num"][i]:
        correct_gender += 1
    else:
        wrong_gender += 1
    if gender + 1 == df["Sex_num"][i] and species + 1 == df["Species_num"][i]:
        correct += 1
    else:
        wrong += 1

print(correct / (correct + wrong), wrong / (correct + wrong))

