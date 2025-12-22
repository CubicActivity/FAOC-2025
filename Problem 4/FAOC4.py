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
