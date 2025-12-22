# Week 4: The Phantom Building
# It has been 10 years. The Dean claims the new FINKI building exists on a secret blueprint, hidden within a labyrinth of bureaucracy and construction fences.
#
# You have obtained a satellite scan of the supposed construction site represented as a 2D grid:
#
#     'S' is your starting position (The Barracks).
#
# 'E' is the entrance to the New Building.'#' represents concrete walls or bureaucratic red tape (impassable).'.' represents open ground.
# Input Format:
# The first line contains two integers: R (rows) and C (columns).
# The following R lines represent the grid.
#
# Your Task:
# Find the minimum number of steps to get from 'S' to 'E'.
# If the building is (as expected) a lie and cannot be reached, return -1.
# Example Input:
# 5 5
# S..#.
# .#...
# ...#.
# .##..
# ...#E
#
# Explanation:
# Path: (0,0) -> (0,1) -> (0,2) -> (1,2) -> (1,3) -> (1,4) -> (2,4) -> (3,4) -> (4,4)
# Result: 8
from collections import deque

def main():
    with open("user_input.txt", "r") as f:
        rows, cols = map(int, f.readline().split())
        grid = [list(f.readline().strip()) for _ in range(rows)]

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'S':
                start = (r, c)
            elif grid[r][c] == 'E':
                end = (r, c)

    queue = deque([(start[0], start[1], 0)])
    visited = set([start])
    moves = [(-1,0),(1,0),(0,-1),(0,1)]  # up, down, left, right

    while queue:
        x, y, steps = queue.popleft()
        if (x, y) == end:
            print(steps)
            return
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != '#' and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, steps + 1))

    print(-1)

if __name__ == "__main__":
    main()
