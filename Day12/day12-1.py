import re

with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

# . = operational
# # = broken
# ? = unknown


def satisfies_rule(data, nums):
    # check if data satisfies rules from nums
    # continuous_broken = 0
    # index_in_nums = 0
    data = data.strip(".")
    # replace multiple consecutive working with one working
    data = re.sub(r"\.+", ".", data)
    parsed = data.split(".")
    lens = [len(x) for x in parsed]
    # print(lens)
    # print(nums)
    # if len(lens) != len(nums):
    #     return False
    if lens != nums:
        return False

    return True


test_data = ".#...#....###.."
test_nums = [1, 1, 3]
# print(satisfies_rule(test_data, test_nums))


sum = 0
for line in lines:
    data, nums = line.split()
    nums = [int(num) for num in nums.split(",")]
    # need to try all possible replacements of ? with . or #
    # first, find all indices of ?
    indices = [i for i, x in enumerate(data) if x == "?"]

    # for each index, try replacing with . and #
    max = 2 ** len(indices)
    for i in range(max):
        # convert i to binary
        binary = bin(i)[2:]
        # pad with 0s
        binary = "0" * (len(indices) - len(binary)) + binary
        # replace ? with . or #
        new_data = data
        for j in range(len(indices)):
            if binary[j] == "0":
                new_data = new_data[: indices[j]] + "." + new_data[indices[j] + 1 :]
            else:
                new_data = new_data[: indices[j]] + "#" + new_data[indices[j] + 1 :]
        if satisfies_rule(new_data, nums):
            sum += 1
            # print(new_data)
            # print(nums)

# Took about 10s to run
print(sum)
