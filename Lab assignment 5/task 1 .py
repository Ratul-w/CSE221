a=input().split()
n=int(a[0])
m=int(a[1])
grp=[[] for i in range(n+1)]

for i in range(m):
    b=input().split()
    u=int(b[0])
    v=int(b[1])
    grp[u].append(v)
    grp[v].append(u)

for i in range(1,n+1):
    grp[i].sort()


visit=[False] *(n+1)
ord=[]

initial_layer=[1]
visit[1]=True

while initial_layer:
    next=[]
    for u in initial_layer:
        ord.append(u)
        for v in grp[u]:
            if not visit[v]:
                visit[v]=True
                next.append(v)
    initial_layer=next

print(*ord)