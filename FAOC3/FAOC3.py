def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, size, a, b):
    ra = find(parent, a)
    rb = find(parent, b)
    if ra != rb:
        parent[rb] = ra
        size[ra] += size[rb]

def main():
    with open("user_input.txt", "r") as f:
        line = f.readline().strip()

    pairs = line.split(",")

    parent = {}
    size = {}

    for pair in pairs:
        a, b = pair.split("-")
        if a not in parent:
            parent[a] = a
            size[a] = 1
        if b not in parent:
            parent[b] = b
            size[b] = 1
        union(parent, size, a, b)

    max_group = 0
    for user in parent:
        root = find(parent, user)
        max_group = max(max_group, size[root])

    print(max_group)

if __name__ == "__main__":
    main()
