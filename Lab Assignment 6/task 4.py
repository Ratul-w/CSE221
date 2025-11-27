import sys
from collections import deque
 
input = sys.stdin.buffer.readline
 
n = int(input())
graph = [[] for i in range(n + 1)]
 
for i in range(n - 1):
    b=input().split()
    u=int(b[0])
    v=int(b[1])
    graph[u].append(v)
    graph[v].append(u)
 
 
dist = [-1] * (n + 1)
dist[1] = 0
q = deque([1])
farthest_node = 1
 
while q:
    u = q.popleft()
    for v in graph[u]:
        if dist[v] == -1:
            dist[v] = dist[u] + 1
            q.append(v)
            if dist[v] > dist[farthest_node]:
                farthest_node = v
 
h = farthest_node
 
dist = [-1] * (n + 1)
dist[h] = 0
q = deque([h])
farthest_node = h
 
while q:
    u = q.popleft()
    for v in graph[u]:
        if dist[v] == -1:
            dist[v] = dist[u] + 1
            q.append(v)
            if dist[v] > dist[farthest_node]:
                farthest_node = v
 
g = farthest_node
diameter = dist[g]
 
 
print(diameter)
print(h, g)