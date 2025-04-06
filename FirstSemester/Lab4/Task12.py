import sys
from collections import OrderedDict

with open("input12.txt", "r") as file:
    n, m = map(int, file.readline().split())
    commands = [line.strip().split() for line in file]

# OrderedDict для хранения порядка в строю
recruits = OrderedDict()
recruits[1] = [None, None]

output = []

for command in commands:
    if command[0] == "left":
        i, j = map(int, command[1:])
        left, right = recruits[j][0], j
        recruits[i] = [left, right]
        recruits[j][0] = i
        if left is not None:
            recruits[left][1] = i
    elif command[0] == "right":
        i, j = map(int, command[1:])
        left, right = j, recruits[j][1]
        recruits[i] = [left, right]
        recruits[j][1] = i
        if right is not None:
            recruits[right][0] = i
    elif command[0] == "leave":
        i = int(command[1])
        left, right = recruits[i]
        if left is not None:
            recruits[left][1] = right
        if right is not None:
            recruits[right][0] = left
        del recruits[i]
    elif command[0] == "name":
        i = int(command[1])
        left, right = recruits[i]
        output.append(f"{left or 0} {right or 0}")

with open("output12.txt", "w") as file:
    file.write("\n".join(output) + "\n")
