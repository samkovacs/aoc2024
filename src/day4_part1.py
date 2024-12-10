# Advent of Code
# Day 4 - Part 1
# @samkovacs

matrix = []
solution_map = {"X": "M", "M": "A", "A": "S"}
row, col = 0, 0
solutions = 0


def check_solutions(row_index, col_index):
    total = 0
    total += check_up(row_index, col_index)
    print(f"Total is {total} after Check_Up")
    total += check_up_left(row_index, col_index)
    print(f"Total is {total} after check_up_left")
    total += check_up_right(row_index, col_index)
    print(f"Total is {total} after check_up_right")
    total += check_left(row_index, col_index)
    print(f"Total is {total} after check_left")
    total += check_right(row_index, col_index)
    print(f"Total is {total} after check_right")
    total += check_down(row_index, col_index)
    print(f"Total is {total} after check_down")
    total += check_down_left(row_index, col_index)
    print(f"Total is {total} after check_down_left")
    total += check_down_right(row_index, col_index)
    print(f"Total is {total} after check_down_right")
    return total


def check_up(i, j):
    is_solution = 0
    current = matrix[i][j]
    try:
        for x in range(len(solution_map.keys())):
            up = matrix[i - (x + 1)][j]
            print(
                f"Solution Check: Up: {up} Solution Map: {solution_map[current]} X: {x} I: {i-(x+1)} J: {j} Is_Solution: {is_solution}"
            )
            if (
                solution_map[current] == up
                and x == len(solution_map.keys()) - 1
                and i - (x + 1) >= 0
            ):
                is_solution += 1
                break
            elif solution_map[current] == up and x < len(solution_map.keys()) - 1:
                current = up
                continue
            else:
                break
    except IndexError:
        return is_solution
    except KeyError:
        return is_solution

    return is_solution


def check_up_left(i, j):
    is_solution = 0
    current = matrix[i][j]
    try:
        for x in range(len(solution_map.keys())):
            up_left = matrix[i - (x + 1)][j - (x + 1)]
            print(
                f"Solution Check: Up: {up_left} Solution Map: {solution_map[current]} X: {x} I: {i-(x+1)} J: {j-(x+1)} Is_Solution: {is_solution}"
            )
            if (
                solution_map[current] == up_left
                and x == len(solution_map.keys()) - 1
                and j - (x + 1) >= 0
                and i - (x + 1) >= 0
            ):
                is_solution += 1
                break
            elif solution_map[current] == up_left and x < len(solution_map.keys()) - 1:
                current = up_left
                continue
            else:
                break
    except IndexError:
        return is_solution
    except KeyError:
        return is_solution

    return is_solution


def check_up_right(i, j):
    is_solution = 0
    current = matrix[i][j]
    try:
        for x in range(len(solution_map.keys())):
            up_right = matrix[i - (x + 1)][j + (x + 1)]
            if (
                solution_map[current] == up_right
                and x == len(solution_map.keys()) - 1
                and i - (x + 1) >= 0
            ):
                is_solution += 1
                break
            elif solution_map[current] == up_right and x < len(solution_map.keys()) - 1:
                current = up_right
                continue
            else:
                break
    except IndexError:
        return is_solution

    return is_solution


def check_left(i, j):
    is_solution = 0
    current = matrix[i][j]
    try:
        for x in range(len(solution_map.keys())):
            left = matrix[i][j - (x + 1)]
            if (
                solution_map[current] == left
                and x == len(solution_map.keys()) - 1
                and j - (x + 1) >= 0
            ):
                is_solution += 1
                break
            elif solution_map[current] == left and x < len(solution_map.keys()) - 1:
                current = left
                continue
            else:
                break
    except IndexError:
        return is_solution

    return is_solution


def check_right(i, j):
    is_solution = 0
    current = matrix[i][j]
    try:
        for x in range(len(solution_map.keys())):
            right = matrix[i][j + (x + 1)]
            if solution_map[current] == right and x == len(solution_map.keys()) - 1:
                is_solution += 1
                break
            elif solution_map[current] == right and x < len(solution_map.keys()) - 1:
                current = right
                continue
            else:
                break
    except IndexError:
        return is_solution

    return is_solution


def check_down(i, j):
    is_solution = 0
    current = matrix[i][j]
    try:
        for x in range(len(solution_map.keys())):
            down = matrix[i + (x + 1)][j]
            if solution_map[current] == down and x == len(solution_map.keys()) - 1:
                is_solution += 1
                break
            elif solution_map[current] == down and x < len(solution_map.keys()) - 1:
                current = down
                continue
            else:
                break
    except IndexError:
        return is_solution

    return is_solution


def check_down_left(i, j):
    is_solution = 0
    current = matrix[i][j]
    try:
        for x in range(len(solution_map.keys())):
            down_left = matrix[i + (x + 1)][j - (x + 1)]
            if (
                solution_map[current] == down_left
                and x == len(solution_map.keys()) - 1
                and j - (x + 1) >= 0
            ):
                is_solution += 1
                break
            elif (
                solution_map[current] == down_left and x < len(solution_map.keys()) - 1
            ):
                current = down_left
                continue
            else:
                break
    except IndexError:
        return is_solution

    return is_solution


def check_down_right(i, j):
    is_solution = 0
    current = matrix[i][j]
    try:
        for x in range(len(solution_map.keys())):
            down_right = matrix[i + (x + 1)][j + (x + 1)]
            if (
                solution_map[current] == down_right
                and x == len(solution_map.keys()) - 1
            ):
                is_solution += 1
                break
            elif solution_map[current] == down_right and x < len(solution_map.keys()):
                current = down_right
                continue
            else:
                break
    except IndexError:
        return is_solution

    return is_solution


with open("day4_input.txt") as f:
    text = f.readlines()
    for line in text:
        row = list(line)
        row.pop(-1)
        matrix.append(row)

    for row_index, row in enumerate(matrix):
        for col_index, value in enumerate(row):
            print(f"Checking {value} at {row_index} , {col_index}.")
            if value.lower() == "x":
                print(f"{value} is X")
                solutions = solutions + check_solutions(row_index, col_index)
                print("Solutions: ", solutions)
            else:
                print(f"{value} is not X")
                continue

print("Final Num_Solutions: ", solutions)
