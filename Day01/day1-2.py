import re

digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

# digitsString = ["|" + digit for digit in digits]
sum = 0
for i in range(len(lines)):
    # Match with regex all digits using findall
    line = lines[i]
    t1 = t2 = None
    for j in range(len(line)):
        for num, d in enumerate(digits):
            if not t1:
                if line[j].isdigit():
                    t1 = int(line[j])
                elif line[j:].startswith(d):
                    t1 = num + 1
            if not t2:
                if line[-(j + 1)].isdigit():
                    t2 = int(line[-(j + 1)])
                elif line[-(j + 1) :].startswith(d):
                    t2 = num + 1
            if t1 and t2:
                # print(t1, t2)
                combined = int(t1) * 10 + int(t2)
                sum += combined
                break
        if t1 and t2:
            break
print(sum)
