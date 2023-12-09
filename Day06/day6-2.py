with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

time = int(lines[0].split(":")[1].replace(" ", ""))
# print(time, type(time))
distance = int(lines[1].split(":")[1].replace(" ", ""))
# print(distance, type(distance))


# Essentially perform a binary search to find the range of button holds that
# will result in the distance
# Since the distance is a quadratic function of button hold, the range of
# button holds that will result in the distance is a range of consecutive
# integers
# The minimum button hold that will result in the distance is the largest
# integer that satisfies the quadratic equation
# The maximum button hold that will result in the distance is the smallest
# integer that satisfies the quadratic equation
# Thus the difference between those two integers is the number of button holds
# that will result in the distance

# This problem definitely can be solved directly using quadratic formula, but
# I thought I could get this method working faster than I could get the
# quadratic formula approach working, and it ran fast enough for the input (<5 seconds)

# find minimum button hold that will result in distance
min_hold = 1
while min_hold * (time - min_hold) <= distance:
    min_hold *= 2
while min_hold * (time - min_hold) > distance:
    min_hold -= 1
min_hold += 1

# find maximum button hold that will result in distance
max_hold = time - 1
while max_hold * (time - max_hold) <= distance:
    max_hold //= 2
while max_hold * (time - max_hold) > distance:
    max_hold += 1
max_hold -= 1

print(max_hold - min_hold + 1)
