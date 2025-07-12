Ga = input().split()
A = int(Ga[0])
B = int(Ga[1])
c = int(Ga[2])
arr1 = [int(x) for x in input().split()]
arr2 = [int(x) for x in input().split()]

i = 0
j = B - 1

closest_sum = arr1[i] + arr2[j]
closest_i = i
closest_j = j

while i < A and j >= 0:
    current = arr1[i] + arr2[j]
    if abs(current - c) < abs(closest_sum - c):
        closest_sum = current
        closest_i = i
        closest_j = j
    if current < c:
        i += 1
    else:
        j -= 1

print(closest_i + 1, closest_j + 1)