import sys, heapq
input = sys.stdin.buffer.readline

a = input().split()
n = int(a[0])
m = int(a[1])

u = [int(x) for x in input().split()]
v = [int(x) for x in input().split()]
w = [int(x) for x in input().split()]


adj = [[] for _ in range(n + 1)]
for i in range(m):
    adj[u[i]].append((v[i], w[i]))

inf = float("inf")

dist0 = [inf] * (n + 1)
dist1 = [inf] * (n + 1)

dist0[1] = 0
dist1[1] = 0

heap = [(0, 1, 0), (0, 1, 1)]
heappush = heapq.heappush
heappop  = heapq.heappop

best = inf

while heap:
    d0, u0, p0 = heappop(heap)
    if p0 == 0:
        if d0 != dist0[u0]:
            continue
    else:
        if d0 != dist1[u0]:
            continue
    if u0 == n:
        if d0 < best:
            best = d0

        if heap and heap[0][0] >= best:
            break
    for v2, w2 in adj[u0]:
        par = w2 & 1
        if par == p0:
            continue
        nd = d0 + w2
        if par == 0:
            if nd < dist0[v2]:
                dist0[v2] = nd
                heappush(heap, (nd, v2, 0))
        else:
            if nd < dist1[v2]:
                dist1[v2] = nd
                heappush(heap, (nd, v2, 1))

if dist0[n] < dist1[n]:
    ans = dist0[n]
else:
    ans = dist1[n]

if ans < inf:
    print(ans)
else:
    print(-1)