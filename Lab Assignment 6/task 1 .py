from collections import deque 
import sys 
input = sys.stdin.buffer.readline
 
c = input().split()
n = int(c[0])
m = int(c[1])
 
graph = [[] for i in range(n + 1)]
indegree = [0] * (n + 1)
 
for i in range(m):
    d = input().split()
    a = int(d[0])
    b = int(d[1])
    graph[a].append(b)
    indegree[b] += 1
 
queue = deque()
for i in range(1, n + 1):
    if indegree[i] == 0:
        queue.append(i)
 
order = []
 
while queue:
    u = queue.popleft()   
    order.append(u)
    for v in graph[u]:
        indegree[v] -= 1
        if indegree[v] == 0:
            queue.append(v)
 
if len(order) == n:
    print(*order)
else:
    print(-1)