H = int(input())
empty = []
for i in range(H):
    ha = input().split()
    k = int(ha[0])
    c = int(ha[1])
    low = 1
    high = k * c
    while low < high:
        mid = (low + high) // 2
        if mid - mid // c >= k:
            high = mid
        else:
            low = mid + 1
    empty.append(low)

for r in empty:
    print(r)