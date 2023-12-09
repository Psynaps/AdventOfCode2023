with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

seq = lines[0]
# print(seq)

nodes = {}
for line in lines[2:]:
    components = line.split()
    node = components[0]
    left = components[2].replace("(", "").replace(",", "")
    right = components[3].replace(")", "")
    # print(node, left, right)
    nodes[node] = (left, right)

# print(nodes)

cur = "AAA"
end = "ZZZ"
step = 0
while cur != end:
    if seq[step % len(seq)] == "L":
        cur = nodes[cur][0]
    else:
        cur = nodes[cur][1]
    step += 1
    # print(cur, step)
print(step)
