a=input().split()
n=int(a[0])
m=int(a[1])
k=int(a[2])
bo=[[0] * (m+1) for i in range(n+1) ]
moves=[]
for i in range(k):
    k_inp=input().split()
    x=int(k_inp[0])
    y=int(k_inp[1])
    bo[x][y]=1
    moves.append((x,y))

pattern=[(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1) ]
fo=False
for x,y in moves:
  for i,j in pattern:
    x_new,y_new=x+i,y+j
    if 1<=x_new<=n and 1<=y_new<=m:
      if bo[x_new][y_new]==1:
       print("YES")
       fo=True
       break
  if fo:
      break
if not fo:
    print("NO")