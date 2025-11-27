a=input().split()
b=int(a[0])
c=int(a[1])
u_in=[int(x) for x in input().split()]
v_in=[int(x) for x in input().split()]
u=[]
for i in range(c):
    u.append(u_in[i])
v=[]
for j in range(c):
    v.append(v_in[j])

deg=[]
for i in range(b+1):
    deg.append(0)
for i in range(c):
    deg[u[i]]+=1
for j in range(c):
    deg[v[j]]+=1
co=0
for i in range(1,b+1):
    if deg[i]%2==1:
        co+=1
if co==0 or co==2:
    print("YES")
else:
    print("NO")