# Advent of Code
# Day 1 - Part 2
# @samkovacs

import pandas as pd

df = pd.read_csv("day1_input.txt", engine="python", sep="   ", header=None)
x = df[1].value_counts()
sim_score = 0

for row_val in df[0]:
    sim_score += row_val * x.get(row_val, 0)

print(sim_score)
