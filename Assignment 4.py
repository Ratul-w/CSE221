T = int(input())
for c in range(T):
    n = int(input())
    arr = [int(x) for x in input().split()]

    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            print("NO")
            break
    else:
        print("YES")