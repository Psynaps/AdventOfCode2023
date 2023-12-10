import re
import math

with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

pipes = []
cur_x = 0
cur_y = 0

adj_pipe_1_x = -1
adj_pipe_1_y = -1

for y, line in enumerate(lines):
    start_x = line.find("S")
    if start_x == -1:
        continue
    if line[start_x + 1] == "-" or line[start_x + 1] == "J" or line[start_x + 1] == "7":
        adj_pipe_1_x = start_x + 1
        adj_pipe_1_y = y
        last_move = "R"
        start_y = y
        break
    elif (
        line[start_x - 1] == "-" or line[start_x - 1] == "L" or line[start_x - 1] == "F"
    ):
        adj_pipe_1_x = start_x - 1
        adj_pipe_1_y = y
        last_move = "L"
        start_y = y
        break
    else:
        adj_pipe_1_x = start_x
        adj_pipe_1_y = y + 1
        last_move = "D"
        start_y = y
        break
# print(adj_pipe_1_x, adj_pipe_1_y, last_move)


def next_loc(x, y, last_move):
    # if last move was up
    if last_move == "U":
        if lines[y][x] == "|":
            return (x, y - 1, "U")
        elif lines[y][x] == "7":
            return (x - 1, y, "L")
        elif lines[y][x] == "F":
            return (x + 1, y, "R")
    elif last_move == "D":
        if lines[y][x] == "|":
            return (x, y + 1, "D")
        elif lines[y][x] == "J":
            return (x - 1, y, "L")
        elif lines[y][x] == "L":
            return (x + 1, y, "R")
    elif last_move == "L":
        if lines[y][x] == "-":
            return (x - 1, y, "L")
        elif lines[y][x] == "F":
            return (x, y + 1, "D")
        elif lines[y][x] == "L":
            return (x, y - 1, "U")
    elif last_move == "R":
        if lines[y][x] == "-":
            return (x + 1, y, "R")
        elif lines[y][x] == "7":
            return (x, y + 1, "D")
        elif lines[y][x] == "J":
            return (x, y - 1, "U")
    print("Error: last_move not valid")
    exit()


def print_loop(loop):
    for line in loop:
        print(line)


loop = [["O"] * len(line) for line in lines]
loop[start_y][start_x] = "L"
loop[adj_pipe_1_y][adj_pipe_1_x] = "L"

cur_x = adj_pipe_1_x
cur_y = adj_pipe_1_y
while True:
    cur_x, cur_y, last_move = next_loc(cur_x, cur_y, last_move)
    # print(cur_x, cur_y, last_move)
    if lines[cur_y][cur_x] == "S":
        break
    loop[cur_y][cur_x] = "L"

if last_move == "U":
    if (
        lines[start_y][start_x + 1] == "-"
        or lines[start_y][start_x + 1] == "J"
        or lines[start_y][start_x + 1] == "7"
    ):
        # print(lines[start_y], lines[start_y][start_x])
        lines[start_y] = lines[start_y].replace("S", "F")
    elif (
        lines[start_y][start_x - 1] == "-"
        or lines[start_y][start_x - 1] == "L"
        or lines[start_y][start_x - 1] == "F"
    ):
        lines[start_y] = lines[start_y].replace("S", "7")
    elif lines[start_y - 1][start_x] == "|":
        lines[start_y] = lines[start_y].replace("S", "|")
elif last_move == "D":
    if (
        lines[start_y][start_x + 1] == "-"
        or lines[start_y][start_x + 1] == "J"
        or lines[start_y][start_x + 1] == "7"
    ):
        lines[start_y] = lines[start_y].replace("S", "L")
    elif (
        lines[start_y][start_x - 1] == "-"
        or lines[start_y][start_x - 1] == "L"
        or lines[start_y][start_x - 1] == "F"
    ):
        lines[start_y] = lines[start_y].replace("S", "J")
    elif lines[start_y + 1][start_x] == "|":
        lines[start_y] = lines[start_y].replace("S", "|")
elif last_move == "L":
    if (
        lines[start_y - 1][start_x] == "|"
        or lines[start_y - 1][start_x] == "F"
        or lines[start_y - 1][start_x] == "7"
    ):
        lines[start_y] = lines[start_y].replace("S", "L")
    elif (
        lines[start_y + 1][start_x] == "|"
        or lines[start_y + 1][start_x] == "F"
        or lines[start_y + 1][start_x] == "7"
    ):
        lines[start_y] = lines[start_y].replace("S", "J")
    elif lines[start_y][start_x - 1] == "-":
        lines[start_y] = lines[start_y].replace("S", "-")
elif last_move == "R":
    if (
        lines[start_y - 1][start_x] == "|"
        or lines[start_y - 1][start_x] == "F"
        or lines[start_y - 1][start_x] == "7"
    ):
        lines[start_y] = lines[start_y].replace("S", "J")
    elif (
        lines[start_y + 1][start_x] == "|"
        or lines[start_y + 1][start_x] == "F"
        or lines[start_y + 1][start_x] == "7"
    ):
        lines[start_y] = lines[start_y].replace("S", "7")
    elif lines[start_y][start_x + 1] == "-":
        lines[start_y] = lines[start_y].replace("S", "-")
# print_loop(loop)
# hardcode replace S with correct symbol
# lines[start_y] = lines[start_y].replace("S", "7")
# This worked, but I took the time to get the generic version working


sum = 0

for y in range(len(loop)):
    for x in range(len(loop[y])):
        if loop[y][x] != "L":
            if x == 0 or x == len(loop[y]) - 1 or y == 0 or y == len(loop) - 1:
                continue

            crossed = 0
            for i in range(0, x):
                # Count number of vertical pipes to the left which are part of the loop. Odd means its inside the loop
                if loop[y][i] == "L" and (
                    lines[y][i] == "L"
                    or lines[y][i] == "|"
                    or lines[y][i] == "J"
                    or lines[y][i] == "S"
                ):
                    crossed += 1

            if crossed % 2 == 1:
                sum += 1
                loop[y][x] = "I"


# print("---------------")
# print_loop(loop)
print(sum)
# print("---------------")
# print_loop(lines)
# print(loop[5][8])
