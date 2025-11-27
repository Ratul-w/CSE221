from collections import deque
import sys
input=sys.stdin.buffer.readline
 
n = int(input())
a = input().split()
x1, y1, x2, y2 = map(int, a)
 
if (x1, y1) == (x2, y2):
    print(0)
elif n == 1:
    print(-1)
elif n == 3:
    moves = [(1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)]
    q = deque([(x1, y1, 0)])
    vis = {(x1, y1)}
    ans = -1
    found = False
 
    while q and not found:
        x, y, d = q.popleft()
        for i, j in moves:
            n_x, n_y = x + i, y + j
            if 1 <= n_x <= 3 and 1 <= n_y <= 3 and (n_x, n_y) not in vis:
                if (n_x, n_y) == (x2, y2):
                    ans = d + 1
                    found = True
                    break
                vis.add((n_x, n_y))
                q.append((n_x, n_y, d + 1))
    print(ans)
else:
    dx, dy = abs(x1 - x2), abs(y1 - y2)
    if dx < dy:
        dx, dy = dy, dx
 
    if dx == 1 and dy == 0:
        print(3)
    elif dx == 2 and dy == 2:
        print(4)
    else:
        d = max((dx + 1) // 2, (dx + dy + 2) // 3)
        if (d + dx + dy) % 2:
            d += 1
        print(d)