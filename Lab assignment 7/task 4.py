import sys, heapq
input = sys.stdin.buffer.readline

a = input().split()
n = int(a[0])
m = int(a[1])
s = int(a[2])
d = int(a[3])


w = [0] + [int(x) for x in input().split()]

adj = [[] for i in range(n + 1)]
for i in range(m):
    x = input().split()
    u = int(x[0])
    v = int(x[1])
    adj[u].append(v)

inf = float("inf")
dist = [inf] * (n + 1)
dist[s] = w[s]

heap = [(w[s], s)]
heappush = heapq.heappush
heappop = heapq.heappop

while heap:
    d0, u0 = heappop(heap)
    if d0 != dist[u0]:
        continue
    if u0 == d:
        break
    for v2 in adj[u0]:
        nd = d0 + w[v2]
        if nd < dist[v2]:
            dist[v2] = nd
            heappush(heap, (nd, v2))

if dist[d] < inf:
    print(dist[d])
else:
    print(-1)