import math

with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

times = [int(time) for time in lines[0].split()[1:]]
distances = [int(distance) for distance in lines[1].split()[1:]]

# print(times)
# print(distances)

num_combinations = [0] * len(times)
for i, time in enumerate(times):
    min_distance = distances[i]
    for speed in range(
        1, time
    ):  # exclude 0 time and full duration time since boat never moves
        if speed * (time - speed) > min_distance:
            num_combinations[i] += 1

# print product of all num_combinations
print(math.prod(num_combinations))
