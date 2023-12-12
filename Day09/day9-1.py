with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]


def all_zeroes(seq):
    for num in seq:
        if num != 0:
            return False
    return True


sum = 0
for line in lines:
    seq = [int(num) for num in line.split()]
    # print(seq)
    all_derivs = []
    all_derivs.append([seq[i + 1] - seq[i] for i in range(len(seq) - 1)])

    while not all_zeroes(all_derivs[-1]):
        derivs = [
            all_derivs[-1][i + 1] - all_derivs[-1][i]
            for i in range(len(all_derivs[-1]) - 1)
        ]
        all_derivs.append(derivs)

    next = seq[-1]
    for i in range(len(all_derivs)):
        next += all_derivs[i][-1]
    sum += next

print(sum)
