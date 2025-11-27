m=input().split()
a=int(m[0])
b=int(m[1])
mat=[[0]*a for i in range(a)]
for j in range(b):
    grap=input().split()
    u=int(grap[0])
    v=int(grap[1])
    w=int(grap[2])
    mat[u - 1][v - 1] = w

for r in mat:
    print(' '.join(map(str, r)))