# Advent of Code
# Day 3 - Part 1
# @samkovacs

import re

total = 0


def mul(a, b):
    return int(a) * int(b)


with open("day3_input.txt") as f:
    text = f.read()
    matches = re.findall(r"mul\([0-9]\d{0,2},[0-9]\d{0,2}\)", text)
    for match in matches:
        a, b = re.findall(r"\d+", match)
        total += mul(a, b)

print(total)
