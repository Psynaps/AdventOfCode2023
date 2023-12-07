with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

numCopies = [1] * len(lines)
for cardNum, line in enumerate(lines):
    line = line.split(":")[1].strip()
    winningNums = line.split("|")[0].strip().split()
    card_nums = line.split("|")[1].strip().split()

    score = 0
    for num in card_nums:
        if num in winningNums:
            score += 1

    for i in range(score):
        numCopies[cardNum + i + 1] += 1 * numCopies[cardNum]

print(sum(numCopies))
