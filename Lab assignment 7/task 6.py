import sys, heapq
input = sys.stdin.buffer.readline

a = input().split()
n = int(a[0])
m = int(a[1])
s = int(a[2])
d = int(a[3])


adj = [[] for _ in range(n + 1)]
for i in range(m):
    x = input().split()
    u = int(x[0])
    v = int(x[1])
    w = int(x[2])
    adj[u].append((v, w))
    adj[v].append((u, w))

inf = float("inf")
dist1 = [inf] * (n + 1)
dist2 = [inf] * (n + 1)  #

dist1[s] = 0
heap = [(0, s)]

heappush = heapq.heappush
heappop  = heapq.heappop

while heap:
    d0, u0 = heappop(heap)

    if d0 > dist2[u0]:
        continue
    for v2, w2 in adj[u0]:
        a1 = d0 + w2

        if a1 < dist1[v2]:

            dist2[v2] = dist1[v2]
            dist1[v2] = a1
            heappush(heap, (a1, v2))
            if dist2[v2] < inf:
                heappush(heap, (dist2[v2], v2))
        elif dist1[v2] < a1 < dist2[v2]:

            dist2[v2] = a1
            heappush(heap, (a1, v2))

ans = dist2[d]
if ans < inf:
    print(ans)
else:
    print(-1)