with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

num = 0
newGrid = []
initialRowLen = len(lines[0])

for line in lines:
    if line.find("#") == -1:
        newGrid.append(line)
        newGrid.append(line)
    else:
        newGrid.append(line)

# cols_added = 0
# find all columns which are empty and store their indices
empty_cols = []
for i in range(initialRowLen):
    empty = True
    for j in range(len(newGrid)):
        if newGrid[j][i] == "#":
            empty = False
            break
    if empty:
        empty_cols.append(i)

# add empty columns at the indices stored in empty_cols
for i in range(len(newGrid)):
    for j in range(len(empty_cols)):
        # insert empty column at index j
        newGrid[i] = (
            newGrid[i][: empty_cols[j] + j] + "." + newGrid[i][empty_cols[j] + j :]
        )


# for line in newGrid:
#     print(line)


galaxies = {}
galaxy_num = 0
for i in range(len(newGrid)):
    for j in range(len(newGrid[i])):
        if newGrid[i][j] == "#":
            galaxies[galaxy_num] = (i, j)
            galaxy_num += 1

# print(galaxies)

# find sum of distance between all pairs of galaxies
sum = 0
for i in range(len(galaxies)):
    for j in range(i + 1, len(galaxies)):
        sum += abs(galaxies[i][0] - galaxies[j][0]) + abs(
            galaxies[i][1] - galaxies[j][1]
        )

print(sum)
