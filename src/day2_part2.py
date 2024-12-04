# Advent of Code
# Day 2 - Part 2
# @samkovacs

safe_reports = 0


def check_line(line, direction):
    safe = 1
    while len(line) > 1:
        i = int(line.pop(0))
        j = int(line.pop(0))
        line.insert(0, str(j))
        if i == j:
            safe = 0
            i = ""
            j = ""
            break
        elif i > j and direction != "increasing" and (1 <= abs(i - j) <= 3):
            direction = "decreasing"
            continue
        elif i < j and direction != "decreasing" and (1 <= abs(i - j) <= 3):
            direction = "increasing"
            continue
        else:
            safe = 0
            i = ""
            j = ""
            break
    return safe


with open("day2_input.txt") as f:
    for line in f:
        direction = ""
        line = line.split()
        line_copy = line.copy()
        safe = check_line(line, direction)
        if safe:
            safe_reports += 1
        else:
            for x in range(len(line_copy)):
                line = line_copy.copy()
                line.pop(x)
                safe = check_line(line, direction)
                if safe:
                    safe_reports += 1
                    break
                else:
                    continue


print(safe_reports)
