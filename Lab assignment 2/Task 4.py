a = int(input())
arr1 = [int(x) for x in input().split()]
b = int(input())
arr2 = [int(x) for x in input().split()]

i = j = 0
empty = []
while i < a and j < b:
    if arr1[i] <= arr2[j]:
        empty.append(str(arr1[i]))
        i += 1
    else:
        empty.append(str(arr2[j]))
        j += 1
while i < a:
    empty.append(str(arr1[i]))
    i += 1

while j < b:
    empty.append(str(arr2[j]))
    j += 1

print(' '.join(empty))