import sys, heapq
input = sys.stdin.buffer.readline

a = input().split()
n = int(a[0])
m = int(a[1])
s = int(a[2])
d = int(a[3])

u = [int(i) for i in input().split()]
v = [int(i) for i in input().split()]
w = [int(i) for i in input().split()]

adj = [[] for _ in range(n + 1)]
for i in range(m):
    adj[u[i]].append((v[i], w[i]))

inf = float("inf")
dist = [inf] * (n + 1)
par = [-1] * (n + 1)
vis = [False] * (n + 1)

dist[s] = 0
pq = [(0, s)]

while pq:
    d0, u0 = heapq.heappop(pq)
    if vis[u0]:
        continue
    vis[u0] = True
    if u0 == d:
        break
    for v2, w2 in adj[u0]:
        nd = d0 + w2
        if nd < dist[v2]:
            dist[v2] = nd
            par[v2] = u0
            heapq.heappush(pq, (nd, v2))

if dist[d] == inf:
    print(-1)
else:
    path = []
    cur = d
    while cur != -1:
        path.append(cur)
        if cur == s:
            break
        cur = par[cur]
    if path[-1] != s:
        print(-1)
    else:
        path.reverse()
        print(dist[d])
        print(*path)