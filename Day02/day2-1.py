import re

with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

maxRed = 12
maxGreen = 13
maxBlue = 14
sum = 0

for line in lines:
    gameID = line.split(" ")[1][:-1]
    # games = line.split(": ")[1].split(";")

    reds = re.findall(r"(\d+) red", line)
    greens = re.findall(r"(\d+) green", line)
    blues = re.findall(r"(\d+) blue", line)

    gameValid = True
    for numReds in reds:
        if int(numReds) > maxRed:
            gameValid = False
            break
    for numGreens in greens:
        if int(numGreens) > maxGreen:
            gameValid = False
            break
    for numBlues in blues:
        if int(numBlues) > maxBlue:
            gameValid = False
            break
    if gameValid:
        sum += int(gameID)
print(sum)
