n=int(input())
emp=[[0]*n for i in range(n)]
for i in range(n):
    inp=[int(x) for x in input().split()]
    st=(inp[0])
    has_n=(inp[1:])
    for j in has_n:
        emp[i][j]=1

for j in emp:
    print(*j )