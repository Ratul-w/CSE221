import sys, heapq

input = sys.stdin.buffer.readline
a = input().split()
n = int(a[0])
m = int(a[1])
s = int(a[2])
t = int(a[3])
adj = [[] for _ in range(n + 1)]
for i in range(m):
    x = input().split()
    u = int(x[0])
    v = int(x[1])
    w = int(x[2])
    adj[u].append((v, w))

inf = float("inf")

distS = [inf] * (n + 1)
visS = [False] * (n + 1)
distS[s] = 0
pq = [(0, s)]
while pq:
    d0, u0 = heapq.heappop(pq)
    if visS[u0]:
        continue
    visS[u0] = True
    for v2, w2 in adj[u0]:
        nd = d0 + w2
        if nd < distS[v2]:
            distS[v2] = nd
            heapq.heappush(pq, (nd, v2))

distT = [inf] * (n + 1)
visT = [False] * (n + 1)
distT[t] = 0
pq = [(0, t)]
while pq:
    d0, u0 = heapq.heappop(pq)
    if visT[u0]:
        continue
    visT[u0] = True
    for v2, w2 in adj[u0]:
        nd = d0 + w2
        if nd < distT[v2]:
            distT[v2] = nd
            heapq.heappush(pq, (nd, v2))

best_time = inf
best_node = -1
for x in range(1, n + 1):
    if distS[x] != inf and distT[x] != inf:
        mt = distS[x] if distS[x] >= distT[x] else distT[x]
        if mt < best_time or (mt == best_time and x < best_node):
            best_time = mt
            best_node = x

if best_node == -1:
    print(-1)
else:
    print(best_time, best_node)