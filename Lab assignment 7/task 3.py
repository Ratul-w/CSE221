import sys, heapq
input = sys.stdin.buffer.readline

a = input().split()
n = int(a[0])
m = int(a[1])

adj = [[] for _ in range(n + 1)]
for i in range(m):
    x = input().split()
    u = int(x[0])
    v = int(x[1])
    w = int(x[2])
    adj[u].append((v, w))
    adj[v].append((u, w))

inf = float("inf")
dist = [inf] * (n + 1)

dist[1] = 0
heap = [(0, 1)]

heappush = heapq.heappush
heappop = heapq.heappop

while heap:
    d0, u0 = heappop(heap)
    if d0 != dist[u0]:
        continue
    for v2, w2 in adj[u0]:
        nd = d0 if d0 >= w2 else w2
        if nd < dist[v2]:
            dist[v2] = nd
            heappush(heap, (nd, v2))

out = []
for i in range(1, n + 1):
    if i == 1:
        out.append("0")
    else:
        if dist[i] < inf:
            out.append(str(dist[i]))
        else:
            out.append("-1")

print(*out)