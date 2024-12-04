# Advent of Code
# Day 2 - Part 1
# @samkovacs

safe_reports = 0

with open("day2_input.txt") as f:
    for line in f:
        safe_reports += 1
        direction = ""
        line = line.split()
        while len(line) > 1:
            print(line)
            i = int(line.pop(0))
            print(line)
            j = int(line.pop(0))
            print(line)
            line.insert(0, str(j))
            print(line)
            if i == j:
                print("they were equal")
                safe_reports -= 1
                i = ""
                j = ""
                break
            elif i > j and direction != "increasing" and (1 <= abs(i - j) <= 3):
                print("we're decreasing")
                direction = "decreasing"
                continue
            elif i < j and direction != "decreasing" and (1 <= abs(i - j) <= 3):
                print("we're increasing")
                direction = "increasing"
                continue
            else:
                print("not safe")
                safe_reports -= 1
                i = ""
                j = ""
                break

print(safe_reports)
