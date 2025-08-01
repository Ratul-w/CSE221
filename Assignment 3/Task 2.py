import bisect


def merge_pair(left, right):
    count = 0
    merged = []
    i = 0
    j = 0

    for val in right:
        sqt = val * val
        idx = bisect.bisect_right(left, sqt)
        count += len(left) - idx

    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    while i < len(left):
        merged.append(left[i])
        i += 1
    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged, count


def mergeSort(arr, n):
    if n <= 1:
        return arr, 0
    else:
        mid = n // 2
        left, left_count = mergeSort(arr[:mid], mid)
        right, right_count = mergeSort(arr[mid:], n - mid)
        merged, cross_count = merge_pair(left, right)
        return merged, left_count + right_count + cross_count


N = int(input())
Arr = [int(x) for x in input().split()]

_, result = mergeSort(Arr, N)
print(result)