# Advent of Code
# Day 4 - Part 2
# @samkovacs

matrix = []
num_solutions = 0

with open("day4_input.txt") as f:
    text = f.readlines()
    for line in text:
        line = list(line)
        line.pop(-1)
        matrix.append(line)

    for row_index, row in enumerate(matrix):
        for col_index, value in enumerate(row):
            if value.lower() == "a":
                if (row_index - 1 < 0) or (col_index - 1 < 0):
                    continue
                else:
                    try:
                        up_left = matrix[row_index - 1][col_index - 1]
                    except IndexError:
                        continue
                    try:
                        up_right = matrix[row_index - 1][col_index + 1]
                    except IndexError:
                        continue
                    try:
                        down_left = matrix[row_index + 1][col_index - 1]
                    except IndexError:
                        continue
                    try:
                        down_right = matrix[row_index + 1][col_index + 1]
                    except IndexError:
                        continue
                    if (
                        (up_left.lower() == "a")
                        or (up_right.lower() == "a")
                        or (down_left.lower() == "a")
                        or (down_right.lower() == "a")
                    ):
                        continue
                    elif (
                        (up_left.lower() == "x")
                        or (up_right.lower() == "x")
                        or (down_left.lower() == "x")
                        or (down_right.lower() == "x")
                    ):
                        continue
                    elif (up_left == down_right) or (up_right == down_left):
                        continue
                    else:
                        num_solutions += 1
                        print(num_solutions)
                        print([up_left, ".", up_right])
                        print()
                        print([".", value, "."])
                        print()
                        print([down_left, ".", down_right])

print(num_solutions)
