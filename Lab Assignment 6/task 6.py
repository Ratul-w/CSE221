from collections import deque
import sys
input=sys.stdin.buffer.readline
a=input().split()
n=int(a[0])
m=int(a[1])
s=int(a[2])
q=int(a[3])
adj=[[] for i in range(n+1)]
for i in range(m):
  b=input().split()
  u=int(b[0])
  v=int(b[1])
  adj[u].append(v)
  adj[v].append(u)
st=[]
s1=[int(x) for x in input().split()]
for i in s1:
  st.append(i)
des=[]
d1= [int(x) for x in input().split()]
for i in d1:
  des.append(i)
dist=[-1]*(n+1)
double=deque()
for i in st:
    dist[i]=0
    double.append(i)
while double:
  ve=double.popleft()
  for i in adj[ve]:
      if dist[i]==-1:
          dist[i]=dist[ve]+1
          double.append(i)
lst=[]
for i in des:
  lst.append(dist[i])
print(*lst)