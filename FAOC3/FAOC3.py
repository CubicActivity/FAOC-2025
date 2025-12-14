# Week 3: The Gossip Protocol,
# The FINKI Discord regulars are spreading rumors about the upcoming exam results.
#
# The rumor spreads via Direct Messages (DMs). If User A DMs User B, they share all the information they know. This is transitive: if A talks to B, and B talks to C, then A, B, and C all know the same rumors.
#
# We have a log of all DMs that happened today. Each user is identified by a unique ID.
#
# Input Format:
# A single line containing a list of DM pairs separated by commas. Each pair is separated by a hyphen.
# Example: "1-2,2-3,5-6" means User 1 talked to User 2, User 2 talked to User 3, and User 5 talked to User 6.
#
# Your Task:
# Identify the separate groups of students sharing rumors. Return the size of the largest group of students who all share the same rumor.
#
# Example Input:
# 1-2,2-3,4-5
#
# Explanation:
# Group 1: {1, 2, 3} (Size 3)
# Group 2: {4, 5} (Size 2)
# Result: 3
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
