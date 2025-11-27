n=int(input())
a=input().split()
x=int(a[0])
y=int(a[1])

pattern=[(0,-1), (0,1),(1,-1),(1,0),(1,1),(-1,-1),(-1,0),(-1,1) ]
moves=[]
for i,j in pattern:
    x_new,y_new=x+i,y+j
    if x_new>=1 and x_new<=n:
        if y_new>=1 and y_new<=n:
            moves.append((x_new,y_new))

moves.sort()
print(len(moves))
for a,b in moves:
    print(a,b)