from collections import deque

pattern = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(g, visit, r, h, R, H):
    queue = deque([(r, h)])
    visit[r][h] = True
    collected = 0

    while queue:
        x, y = queue.popleft()

        if g[x][y] == 'D':
            collected += 1
        for dx, dy in pattern:
            nx, ny = x + dx, y + dy
            if 0 <= nx < R and 0 <= ny < H:
                if not visit[nx][ny] and g[nx][ny] != '#':
                    visit[nx][ny] = True
                    queue.append((nx, ny))

    return collected

def max_diamonds(R, H, g):
    visited = [[False] * H for i in range(R)]
    max_d = 0
    for i in range(R):
        for j in range(H):
            if g[i][j] != '#' and not visited[i][j]:
                collected = bfs(g, visited, i, j, R, H)
                max_d = max(max_d, collected)

    return max_d

R, H =[int(x) for x in input().split()]
g = [input().strip() for i in range(R)]
print(max_diamonds(R, H, g))