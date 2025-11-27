from collections import deque
import sys
input=sys.stdin.buffer.readline
b=input().split()
n=int(b[0])
m=int(b[1])

graph=[[] for i in range(n+1)]

for i in range(m):
    b=input().split()
    u=int(b[0])
    v=int(b[1])
    graph[u].append(v)
    graph[v].append(u)
color=[-1]*(n+1)
total=0
for i in range(1,n+1):
    if color[i]==-1:
        queue=deque([i])
        color[i]=0
        cnt=[1,0]
        while queue:
            u=queue.popleft()
            for v in graph[u]:
                if color[v]==-1:
                    color[v]=1-color[u]
                    cnt[color[v]]+=1
                    queue.append(v)
                elif color[v]==color[u]:
                    pass
        total+=max(cnt)

print(total)