# Advent of Code
# Day 4 - Part 2
# @samkovacs

matrix = []
sams = []
num_solutions = 0

with open("day4_testinput.txt") as f:
    text = f.readlines()
    for line in text:
        row = list(line)
        row.pop(-1)
        matrix.append(row)

    print(matrix)

    for row_index, row in enumerate(matrix):
        for col_index, value in enumerate(row):
            print(f" value is {value.lower()}")
            if value.lower() == "s":
                if (
                    row_index + 2 < len(matrix[row_index])
                    and matrix[row_index + 2][col_index].lower() == "s"
                ):
                    print(
                        f"Checking {matrix[row_index + 2][col_index].lower()} is equal to {value.lower()} (Row_Index: {row_index+1} Col_Index: {col_index+1} Len_Matrix: {len(matrix[row_index])}"
                    )
                    if (
                        col_index + 1 < len(matrix[row_index])
                        and row_index + 1 < len(matrix[row_index])
                        and matrix[row_index + 1][col_index + 1].lower() == "a"
                    ):
                        print(
                            f"Checking {matrix[row_index+1][col_index+1].lower()} is equal to a"
                        )
                        if (
                            col_index + 2 < len(matrix[row_index])
                            and row_index + 2 < len(matrix[row_index])
                            and matrix[row_index][col_index + 2].lower() == "m"
                            and matrix[row_index + 2][col_index + 2].lower() == "m"
                        ):
                            print("Solution Found: ", num_solutions)
                            num_solutions += 1
                        else:
                            print("nope")
                            continue
                    elif (
                        col_index - 1 >= 0
                        and row_index + 1 < len(matrix[row_index])
                        and matrix[row_index + 1][col_index - 1].lower() == "a"
                    ):
                        print(
                            f"Checking {matrix[row_index +1][col_index-1].lower()} is equal to a. Col_Index: {col_index-1}"
                        )
                        if (
                            row_index + 2 < len(matrix[row_index])
                            and col_index - 2 >= 0
                            and matrix[row_index][col_index - 2].lower() == "m"
                            and matrix[row_index + 2][col_index - 2].lower() == "m"
                        ):
                            print("Solution Found: ", num_solutions)
                            num_solutions += 1
                        else:
                            print("nope")
                            continue
                    else:
                        print("nope")
                        continue
                else:
                    continue
                if (
                    col_index + 2 < len(matrix[row_index])
                    and matrix[row_index][col_index + 2].lower() == "s"
                ):
                    if (
                        row_index + 1 < len(matrix[row_index])
                        and col_index + 1 < len(matrix[row_index])
                        and matrix[row_index + 1][col_index + 1].lower() == "a"
                    ):
                        if (
                            row_index + 2 < len(matrix[row_index])
                            and col_index + 2 < len(matrix[row_index])
                            and matrix[row_index + 2][col_index].lower() == "m"
                            and matrix[row_index + 2][col_index + 2].lower() == "m"
                        ):
                            num_solutions += 1
                        else:
                            continue
                    elif (
                        row_index - 1 >= 0
                        and col_index < len(matrix[row_index])
                        and matrix[row_index - 1][col_index + 1].lower() == "a"
                    ):
                        if (
                            row_index - 2 >= 0
                            and col_index + 2 < len(matrix[row_index])
                            and matrix[row_index - 2][col_index].lower() == "m"
                            and matrix[row_index - 2][col_index + 2].lower() == "m"
                        ):
                            num_solutions += 1
                        else:
                            continue
                    else:
                        continue
print(num_solutions)
