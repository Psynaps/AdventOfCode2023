from functools import cache

with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

# . = operational
# # = broken
# ? = unknown


@cache
def get_num_solutions(data, counts, index, hashes_seen, index_in_counts):
    if index == len(data):
        if index_in_counts == len(counts):
            ret = 1
        else:
            ret = 0
    elif data[index] == "#":
        ret = get_num_solutions(
            data, counts, index + 1, hashes_seen + 1, index_in_counts
        )
    elif data[index] == "." or index_in_counts == len(counts):
        if index_in_counts < len(counts) and hashes_seen == counts[index_in_counts]:
            ret = get_num_solutions(data, counts, index + 1, 0, index_in_counts + 1)
        elif hashes_seen == 0:
            ret = get_num_solutions(data, counts, index + 1, 0, index_in_counts)
        else:
            ret = 0
    else:
        hashes = get_num_solutions(
            data, counts, index + 1, hashes_seen + 1, index_in_counts
        )
        dots = 0
        if hashes_seen == counts[index_in_counts]:
            dots = get_num_solutions(data, counts, index + 1, 0, index_in_counts + 1)
        elif hashes_seen == 0:
            dots = get_num_solutions(data, counts, index + 1, 0, index_in_counts)
        ret = hashes + dots
    return ret


# test_data = ".#...#....###.."
# test_nums = [1, 1, 3]
# print(satisfies_rule(test_data, test_nums))


sum = 0
# lines = ["???.### 1,1,3", ".??..??...?##. 1,1,3"]
for line in lines:
    # print(line)
    data, nums = line.split()
    # replace data with 5 copies of data separated by ?
    data = "?".join((data, data, data, data, data)) + "."
    # add trailing period to handle last number same as others
    nums = tuple([int(num) for num in nums.split(",")] * 5)
    # print(type(tuple(nums)))
    # print(data)
    # print(nums)

    combinations = get_num_solutions(data, nums, 0, 0, 0)
    # combinations = getcount(data, nums, 0, 0, 0)
    # print(combinations)
    sum += combinations

# Took about 10s to run
print(sum)
