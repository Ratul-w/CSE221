n_x = input().split()
n = int(n_x[0])
x = int(n_x[1])
arr = [int(i) for i in input().split()]

arr_with_index = [(arr[i], i + 1) for i in range(n)]
arr_with_index.sort()
found = False
for i in range(n - 2):
    a = arr_with_index[i][0]
    left = i + 1
    right = n - 1
    while left < right:
        b = arr_with_index[left][0]
        c = arr_with_index[right][0]
        total = a + b + c
        if total == x:
            print(arr_with_index[i][1], arr_with_index[left][1], arr_with_index[right][1])
            found = True
            break
        elif total < x:
            left += 1
        else:
            right -= 1
    if found:
        break

if not found:
    print(-1)