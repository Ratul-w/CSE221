n = int(input())
arr = [int(x) for x in input().split()]

even_part = [arr[i] for i in range(0, n, 2)]
odd_part = [arr[i] for i in range(1, n, 2)]
even_part.sort()
odd_part.sort()

merged = []
ei, oi = 0, 0
for i in range(n):
    if i % 2 == 0:
        merged.append(even_part[ei])
        ei += 1
    else:
        merged.append(odd_part[oi])
        oi += 1
for i in range(n - 1):
    if merged[i] > merged[i + 1]:
        print("NO")
        break
else:
    print("YES")