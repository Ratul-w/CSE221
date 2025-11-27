def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

a = input().split()
n = int(a[0])
m = int(a[1])
emp = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i < j and gcd(i, j) == 1:
            emp[i].append(j)
            emp[j].append(i)

for j in emp:
    j.sort()

for i in range(m):
    b = input().split()
    c = int(b[0])
    d = int(b[1])
    if d <= len(emp[c]):
        print(emp[c][d - 1])
    else:
        print(-1)