add = input().split()
n = int(add[0])
k = int(add[1])
arr = [int(x) for x in input().split()]

freq = [0] * (n + 1)
l = 0
dist = 0
long = 0

for r in range(n):
    if freq[arr[r]] == 0:
        dist += 1
    freq[arr[r]] += 1

    while dist > k:
        freq[arr[l]] -= 1
        if freq[arr[l]] == 0:
            dist -= 1
        l += 1

    if r - l + 1 > long:
        long = r - l + 1

print(long)