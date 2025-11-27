from collections import deque

def bfs(graph, start, end, n):
    dist = [-1] * (n + 1)
    parent = [-1] * (n + 1)
    queue = deque([start])
    dist[start] = 0

    while queue:
        node = queue.popleft()
        if node == end:
            break
        for nei in graph[node]:
            if dist[nei] == -1:
                dist[nei] = dist[node] + 1
                parent[nei] = node
                queue.append(nei)

    if dist[end] == -1:
        return -1, []

    lst = []
    current = end
    while current != -1:
        lst.append(current)
        current = parent[current]

    lst.reverse()
    return dist[end], lst


def find_path(n, m, s, d, k, edge):
    graph = [[] for _ in range(n + 1)]
    for u, v in edge:
        graph[u].append(v)
    for i in range(1, n + 1):
        graph[i].sort()
    dist1, lst1 = bfs(graph, s, k, n)
    if dist1 == -1:
        return -1, []

    dist2, lst2 = bfs(graph, k, d, n)
    if dist2 == -1:
        return -1, []

    combined_lst = lst1[:-1] + lst2
    return dist1 + dist2, combined_lst



a=input().split()
n=int(a[0])
m=int(a[1])
s=int(a[2])
d=int(a[3])
k=int(a[4])

edge = []
for i in range(m):
    u, v = [int(x) for x in input().split()]
    edge.append((u, v))

dist, lst = find_path(n,m,s,d,k, edge)

if dist == -1:
    print(-1)
else:
    print(dist)
    print(*lst)