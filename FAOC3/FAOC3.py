def dfs(node, graph, visited):
    stack = [node]
    count = 0

    while stack:
        current = stack.pop()
        if current not in visited:
            visited.add(current)
            count += 1
            stack.extend(graph[current] - visited)

    return count

def main():
    with open("user_input.txt", "r") as f:
        line = f.readline().strip()

    pairs = line.split(",")

    graph = {}

    for pair in pairs:
        a, b = pair.split("-")
        graph.setdefault(a, set()).add(b)
        graph.setdefault(b, set()).add(a)

    visited = set()
    max_group = 0

    for user in graph:
        if user not in visited:
            max_group = max(max_group, dfs(user, graph, visited))

    print(max_group)

if __name__ == "__main__":
    main()
