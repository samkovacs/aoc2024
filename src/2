# Advent of Code
# Day 5 - Part 1
# @samkovacs

import sys

rules = []
tests = []
score = 0

with open(sys.argv[1]) as fd:
    for y, line in enumerate(fd):
        line = line.strip().upper()
        r1 = line.split("|")
        r2 = line.split(",")

        if len(r1) == 2:
            rules.append(r1)
        elif len(r2) > 2:
            tests.append(r2)
        else:
            continue

print("Rules: ", rules)
print("Tests: ", tests)
rules_dict = {}

for rule in rules:
    if rule[0] in rules_dict:
        rules_dict[rule[0]].append(rule[1])
    else:
        rules_dict[rule[0]] = [rule[1]]

print("Rules Dict: ", rules_dict)

for y, test in enumerate(tests):
    print("Now Testing: ", test)
    mid_index = (len(test) - 1) / 2
    midpoint = test[int(mid_index)]
    for elem in test:
        print("Checking Elem: ", elem)
        if int(midpoint) == 0:
            print("Previous elem broke the rule.")
            break
        elif elem in rules_dict:
            rule_values = rules_dict[elem]
        else:
            print(f"{elem} not in rules_dict")
            continue
        print("Comparing Rules: ", rule_values)
        for rule_val in rule_values:
            try:
                print(f"Is {elem} before {rule_val} ?")
                if test.index(elem) < test.index(rule_val):
                    print("Yes")
                    continue
                else:
                    print("No")
                    midpoint = 0
                    break
            except KeyError:
                print("Rule Missing")
                continue
            except ValueError:
                print("Rule Missing")
                continue
    print("Success: ", midpoint)
    score += int(midpoint)

print(score)
