st = input().split()
n = int(st[0])
q = int(st[1])
arr = [int(x) for x in input().split()]

for k in range(q):
    second = input().split()
    x = int(second[0])
    y = int(second[1])
    left = 0
    right = n
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] >= x:
            right = mid
        else:
            left = mid + 1
    lower = left
    left = 0
    right = n
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] > y:
            right = mid
        else:
            left = mid + 1
    upper = left

    count = upper - lower
    print(count)