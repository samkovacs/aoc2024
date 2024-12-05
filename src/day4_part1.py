# Advent of Code
# Day 4 - Part 1
# @samkovacs

matrix = []
solution_map = {"x": "m", "m": "a", "a": "s", "s": "a"}
row, col = 0, 0


def check_neighbors(i, j):
    up = matrix[i - 1][j]
    up_left = matrix[i - 1][j - 1]
    up_right = matrix[i - 1][j + 1]
    left = matrix[i][j - 1]
    right = matrix[i][j + 1]
    down = matrix[i + 1][j]
    down_left = matrix[i + 1][j - 1]
    down_right = matrix[i + 1][j + 1]


with open("day4_input.txt") as f:
    text = f.readlines()
    for line in text:
        row = list(line)
        row.pop(-1)
        matrix.append(row)
