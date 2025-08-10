#!/usr/bin/env python3
"""
count_islands.py

Count number of islands in a grid of 'L' (land) and 'W' (water).
Connectivity is 8-directional (N, S, E, W, and 4 diagonals).

Usage:
  python count_islands.py
The script runs a sample test — replace `grid` with your own to test.
"""

from collections import deque

def count_islands(grid):
    """
    Count islands in the grid. Grid is a list of lists of characters 'L' or 'W'.
    Uses iterative DFS (stack) or BFS (queue) to mark visited land cells.
    """
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    visited = [[False]*cols for _ in range(rows)]

    # 8 directions: (dx, dy)
    directions = [(-1,  0), (1,  0), (0, -1), (0, 1),
                  (-1, -1), (-1, 1), (1, -1), (1, 1)]

    def bfs(start_r, start_c):
        q = deque()
        q.append((start_r, start_c))
        visited[start_r][start_c] = True
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if not visited[nr][nc] and grid[nr][nc] == 'L':
                        visited[nr][nc] = True
                        q.append((nr, nc))

    islands = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'L' and not visited[r][c]:
                # found a new island, traverse all connected land
                islands += 1
                bfs(r, c)

    return islands

def print_grid(grid):
    for row in grid:
        print(''.join(row))
    print()

if __name__ == "__main__":
    # Sample input (feel free to edit)
    sample_grid = [
        list("WLLWWWL"),
        list("WLWLWLL"),
        list("WLLWLWW"),
        list("WWLLLWW"),
        list("WWWWWLW"),
    ]

    print("Grid:")
    print_grid(sample_grid)

    result = count_islands(sample_grid)
    print(f"Number of islands: {result}")

    # Another simple test:
    g2 = [
        list("LLLL"),
        list("LWWL"),
        list("LWLW"),
        list("WWLL"),
    ]
    print("Grid 2:")
    print_grid(g2)
    print("Number of islands (grid2):", count_islands(g2))
