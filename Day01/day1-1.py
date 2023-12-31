import re

with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

sum = 0
for line in lines:
    # Match with regex all digits using findall

    # First digit
    digits = re.findall(r"\d", line)
    combined = int(digits[0]) * 10 + int(digits[-1])
    sum += combined
print(sum)
