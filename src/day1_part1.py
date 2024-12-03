# Advent of Code
# Day 1
# @samkovacs

import pandas as pd

df = pd.read_csv("day1_input.txt", engine="python", sep="   ", header=None)
for col in df:
    df[col] = df[col].sort_values(ignore_index=True)

x = abs(df[0] - df[1])
print(x.sum())
