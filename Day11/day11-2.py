with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

num = 0
grid = lines
initialRowLen = len(lines[0])


empty_rows = []
for i, line in enumerate(grid):
    if line.find("#") == -1:
        empty_rows.append(i)

# cols_added = 0
# find all columns which are empty and store their indices
empty_cols = []
for i in range(initialRowLen):
    empty = True
    for j in range(len(grid)):
        if grid[j][i] == "#":
            empty = False
            break
    if empty:
        empty_cols.append(i)

# print(empty_cols)
# print(empty_rows)

galaxies = {}
galaxy_num = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "#":
            galaxies[galaxy_num] = (i, j)
            galaxy_num += 1

# print(galaxies)

multiplier = 1000000
# find sum of distance between all pairs of galaxies
sum = 0
for i in range(len(galaxies)):
    for j in range(i + 1, len(galaxies)):
        sum += abs(galaxies[i][0] - galaxies[j][0]) + abs(
            galaxies[i][1] - galaxies[j][1]
        )
        for r in range(
            min(galaxies[i][0] + 1, galaxies[j][0]),
            max(galaxies[i][0] + 1, galaxies[j][0]),
        ):
            if r in empty_rows:
                sum += multiplier - 1
        for c in range(
            min(galaxies[i][1] + 1, galaxies[j][1]),
            max(galaxies[i][1] + 1, galaxies[j][1]),
        ):
            if c in empty_cols:
                sum += multiplier - 1


print(sum)

# Used to test if the distance between two galaxies is calculated correctly
# g1 = 6
# g2 = 8

# sum = 0
# sum += abs(galaxies[g1][0] - galaxies[g2][0]) + abs(galaxies[g1][1] - galaxies[g2][1])
# for r in range(
#     min(galaxies[g1][0], galaxies[g2][0]), max(galaxies[g1][0], galaxies[g2][0])
# ):
#     if r in empty_rows:
#         print("added")
#         sum += multiplier - 1
# for c in range(
#     min(galaxies[g1][1], galaxies[g2][1]), max(galaxies[g1][1], galaxies[g2][1])
# ):
#     if c in empty_cols:
#         print("added")
#         sum += multiplier - 1
# print(sum)
