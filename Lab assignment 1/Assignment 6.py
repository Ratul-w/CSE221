N = int(input())
arr = [int(x) for x in input().split()]

for j in range(N):
    for i in range(N - 1):
        if arr[i] % 2 == arr[i + 1] % 2 and arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

print(*arr)