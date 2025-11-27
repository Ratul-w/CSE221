a = input().split()
n = int(a[0])
m = int(a[1])
u_in = input().split()
u=[]
for i in range(m):
    u.append(int(u_in[i]))
v_in = input().split()
v=[]
for j in range(m):
    v.append(int(v_in[j]))

in_deg=[]
out_deg=[]
for k in range(n+1):
    in_deg.append(0)
    out_deg.append(0)

for i in range(m):
    in_deg[v[i]]+=1
for j in range(m):
    out_deg[u[j]]+=1

diff=[]

for i in range(1,n+1):
    dif=in_deg[i]-out_deg[i]
    diff.append(str(dif))
print(" ".join(diff))