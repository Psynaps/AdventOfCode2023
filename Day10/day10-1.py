import re
import math

with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

sum = 0
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


loop = [[-2] * len(line) for line in lines]
loop[start_y][start_x] = 0
loop[adj_pipe_1_y][adj_pipe_1_x] = 0

steps = 0
cur_x = adj_pipe_1_x
cur_y = adj_pipe_1_y
while True:
    cur_x, cur_y, last_move = next_loc(cur_x, cur_y, last_move)
    # print(cur_x, cur_y, last_move)
    steps += 1
    if lines[cur_y][cur_x] == "S":
        break
    loop[cur_y][cur_x] = 0

# print("Pipe is,", steps, "steps long")

print(math.floor(steps / 2 + 1))
