def map_ranges(seed_ranges, mapping):
    new_ranges = []
    for seed_start, seed_end in seed_ranges:
        current_start = seed_start
        while current_start <= seed_end:
            mapped = False
            for source_start, source_end, dest_start in mapping:
                if source_start <= current_start <= source_end:
                    # Overlapping part
                    overlap_end = min(seed_end, source_end)
                    mapped_start = dest_start + (current_start - source_start)
                    mapped_end = dest_start + (overlap_end - source_start)
                    new_ranges.append((mapped_start, mapped_end))
                    current_start = overlap_end + 1
                    mapped = True
                    break  # Break after mapping the overlapping part

            if not mapped:
                # No overlap, carry over the range as is
                new_ranges.append((current_start, seed_end))
                break  # Entire remaining range is carried over

    return new_ranges


with open("input.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

seedsPre = [int(seed) for seed in lines[0].split()[1:]]
seed_ranges = [
    (seedsPre[i], seedsPre[i] + seedsPre[i + 1] - 1) for i in range(0, len(seedsPre), 2)
]

maps = []
for line in lines[2:]:
    if "map:" in line:
        maps.append([])
    elif line:
        dest_start, source_start, length = map(int, line.split())
        maps[-1].append((source_start, source_start + length - 1, dest_start))

for map in maps:
    seed_ranges = map_ranges(seed_ranges, map)

# Find the minimum start of the range in the final mapped ranges
min_location = min(r[0] for r in seed_ranges)
print(min_location)
