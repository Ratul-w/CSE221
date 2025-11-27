from collections import deque

n, m = [int(x) for x in input().split()]

adj = [[] for i in range(n + 1)]
inq = [0] * (n + 1)


edges = []
for i in range(m):
    u, v = [int(x) for x in input().split()]
    edges.append((u, v))
    adj[u].append(v)
    inq[v] += 1

queue = deque()
for i in range(1, n + 1):
    if inq[i] == 0:
        queue.append(i)

count = 0
while queue:
    node = queue.popleft()
    count += 1
    for i in adj[node]:
        inq[i] -= 1
        if inq[i] == 0:
            queue.append(i)
if count == n:
    print("NO")
else:
    print("YES")