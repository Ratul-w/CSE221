import sys
sys.setrecursionlimit(2*100000+5)

n,m=[int(x) for x in input().split()]
adj=[[] for i in range(n+1)]
u=[int(i) for i in input().split()]
v=[int(i) for i in input().split()]
for i in range(m):
    adj[u[i]].append(v[i])
    adj[v[i]].append(u[i])

visited=[False] * (n+1)
lst=[]

def dfs (u):
    visited[u]=True
    lst.append(u)
    for v in adj[u]:
        if not visited[v]:
            dfs(v)

dfs(1)
print(*lst)