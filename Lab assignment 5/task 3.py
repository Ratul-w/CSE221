from collections import deque

a = input().split()
n = int(a[0])
m = int(a[1])
s = int(a[2])
d = int(a[3])

u=[int(x) for x in input().split()]
v=[int(x) for x in input().split()]

graph = [[] for i  in range(n + 1)]

for i in range(m):
    graph[u[i]].append(v[i])
    graph[v[i]].append(u[i])

for i in range(1, n + 1):  
    graph[i].sort()

dist = [-1] * (n + 1)
parent = [-1] * (n + 1)

queue = deque([s])
dist[s] = 0

while queue:
    node = queue.popleft()
    for nei in graph[node]:
        if dist[nei] == -1:
            dist[nei] = dist[node] + 1
            parent[nei] = node
            queue.append(nei)

if dist[d] == -1:
    print(-1)
else:
    lst = []
    current = d
    while current != -1:
        lst.append(current)
        current = parent[current]
    lst.reverse()

    print(dist[d])
    print(*lst)