n,r=[int(x) for x in input().split()]
adj=[[] for i in range(n+1)]
for i in range(n-1):
    u,v=[int(x) for x in input().split()]
    adj[u].append(v)
    adj[v].append(u)

parent=[-1]* (n+1)
s=[0]*(n+1)

stack=[r]
visited=[False]*(n+1)
while stack:
    node=stack[-1]
    if visited[node]:
        stack.pop()
        s[node]=1 

        for i in adj[node]:
            if i!=parent[node]:
                s[node]+=s[i]
    else:
        visited[node]=True
        for i in adj[node]:
            if not visited[i]:
                parent[i]=node
                stack.append(i)

y=int(input())
for i in range(y):
    t=int(input())
    print(s[t])