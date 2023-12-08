with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

seeds = [int(seed) for seed in lines[0].split()[1:]]
# print(seeds)

maps = []
mapNum = -1
for line in lines[2:]:
    if "map:" in line:
        mapNum += 1
        maps.append([])
        continue

    if line == "":
        continue

    destStart, sourceStart, rangeLen = [int(num) for num in line.split()]
    # print("Map", mapNum, ":", destStart, sourceStart, rangeLen)
    maps[mapNum].append((destStart, sourceStart, rangeLen))

# print(maps)
locations = []
for seed in seeds:
    dest = seed
    for i in range(len(maps)):
        for destStart, sourceStart, rangeLen in maps[i]:
            # for destStart, sourceStart, rangeLen in map:
            if dest >= sourceStart and dest < sourceStart + rangeLen:
                dest = destStart + dest - sourceStart
                break
    locations.append(dest)
# print(locations)

print(min(locations))
