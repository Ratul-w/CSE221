def merge(a, b):
    merged = []
    i = j = inv_count = 0
    n1, n2 = len(a), len(b)

    while i < n1 and j < n2:
        if a[i] <= b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1
            inv_count += n1 - i

    while i < n1:
        merged.append(a[i])
        i += 1
    while j < n2:
        merged.append(b[j])
        j += 1
    return merged, inv_count


def mergeSort(arr):
    if len(arr) <= 1:
        return arr, 0
    else:
        mid = len(arr) // 2
        a1, inv1 = mergeSort(arr[:mid])
        a2, inv2 = mergeSort(arr[mid:])
        merged, inv_merge = merge(a1, a2)
        return merged, inv1 + inv2 + inv_merge


N = int(input())
arr = [int(x) for x in input().split()]

sort, inv_count = mergeSort(arr)

print(inv_count)
print(*sort)