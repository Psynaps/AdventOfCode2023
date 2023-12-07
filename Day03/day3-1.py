import re

with open("input.txt", "r") as f:
    lines = [
        line.strip() + "." for line in f.readlines()
    ]  # Fix problem of it not checking for the last number in a line by adding extra period


def isSymbol(x):
    return not x.isdigit() and not x == "."


sum = 0
for i, line in enumerate(lines):
    curNum = -1
    numStart = -1
    numEnd = -1
    for j in range(len(line)):
        if line[j].isdigit():
            if numStart == -1:
                numStart = j
            numEnd = j
        else:
            if numStart != -1:
                curNum = int(line[numStart : numEnd + 1])
                # check if number is adjacent, or diagonal to a symbol
                if i > 0:
                    for k in range(
                        max(0, numStart - 1), min(len(lines[i - 1]), numEnd + 2)
                    ):
                        if isSymbol(lines[i - 1][k]):
                            sum += curNum
                            curNum = -1
                            numStart = -1
                            numEnd = -1
                            break
                if i < len(lines) - 1 and curNum != -1:
                    for k in range(
                        max(0, numStart - 1), min(len(lines[i + 1]), numEnd + 2)
                    ):
                        if isSymbol(lines[i + 1][k]):
                            sum += curNum
                            curNum = -1
                            numStart = -1
                            numEnd = -1
                            break
                if (
                    isSymbol(line[max(0, numStart - 1)])
                    or isSymbol(line[min(len(line) - 1, numEnd + 1)])
                    and curNum != -1
                ):
                    sum += curNum
                    curNum = -1
                    numStart = -1
                    numEnd = -1

                numStart = -1
                numEnd = -1
                curNum = -1
print(sum)
