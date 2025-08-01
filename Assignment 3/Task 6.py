def build_bst(arr, left, right, result):
    if left > right:
        return
    mid = (left + right) // 2
    result.append(arr[mid])
    build_bst(arr, left, mid - 1, result)
    build_bst(arr, mid + 1, right, result)


n = int(input())
arr = [int(x) for x in input().split()]
result = []
build_bst(arr, 0, n - 1, result)
print(*result)