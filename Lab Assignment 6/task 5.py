import sys
import heapq

input = sys.stdin.readline

n = int(input())
words = [input().strip() for _ in range(n)]

used = [False] * 26
for w in words:
    for ch in w:
        used[ord(ch) - 97] = True

adj = [[] for _ in range(26)]

indg = [0] * 26
added = [[False] * 26 for _ in range(26)]

checker = True
for i in range(n - 1):
    w1, w2 = words[i], words[i + 1]
    m = min(len(w1), len(w2))
    j = 0
    while j < m and w1[j] == w2[j]:
        j += 1
    if j == m:
        if len(w1) > len(w2): 
            checker = False
        continue
    u, v = ord(w1[j]) - 97, ord(w2[j]) - 97
    if not added[u][v]:
        adj[u].append(v)
        indg[v] += 1
        added[u][v] = True

order = []
if checker:
    heap = []
    for i in range(26):
        if used[i] and indg[i] == 0:
            heapq.heappush(heap, i)

    while heap:
        u = heapq.heappop(heap)
        order.append(chr(u + 97))
        for v in adj[u]:
            indg[v] -= 1
            if indg[v] == 0:
                heapq.heappush(heap, v)

if not checker or len(order) < sum(used):
    print(-1)
else:
    print("".join(order))