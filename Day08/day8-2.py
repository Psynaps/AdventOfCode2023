from math import lcm

with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

seq = lines[0]
# print(seq)

nodes = {}
start_nodes = []
end_nodes = []


for line in lines[2:]:
    components = line.split()
    node = components[0]
    left = components[2].replace("(", "").replace(",", "")
    right = components[3].replace(")", "")
    # print(node, left, right)
    nodes[node] = (left, right)
    if node[-1] == "A":  # ends with A means it is a starting node
        start_nodes.append(node)

# print(nodes)
# print(start_nodes)


def steps_to_end(node):
    step = 0
    cur = node
    while cur[-1] != "Z":
        if seq[step % len(seq)] == "L":
            cur = nodes[cur][0]
        else:
            cur = nodes[cur][1]
        step += 1
    return step


# for each start node, find their steps to end
# the answer is the lcm of all these steps, since that is when all the nodes will be at the end

steps = [steps_to_end(node) for node in start_nodes]
print(lcm(*steps))
