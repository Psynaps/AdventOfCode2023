import re

with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

maxRed = 12
minGreen = 13
minBlue = 14

sum = 0
for line in lines:
    minRed = minGreen = minBlue = None
    gameID = line.split(" ")[1][:-1]

    reds = re.findall(r"(\d+) red", line)
    reds = [int(num) for num in reds]

    greens = re.findall(r"(\d+) green", line)
    greens = [int(num) for num in greens]

    blues = re.findall(r"(\d+) blue", line)
    blues = [int(num) for num in blues]

    minRed = max(reds) if reds else 0
    minGreen = max(greens) if greens else 0
    minBlue = max(blues) if blues else 0

    power = minRed * minGreen * minBlue
    sum += power
print(sum)
