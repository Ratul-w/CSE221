A_B = input().split()
A = int(A_B[0])
B = int(A_B[1])

arr = [int(x) for x in input().split()]

left = 0
sum_ = 0
maxLength = 0

for i in range(A):
    sum_ += arr[i]

    while sum_ > B and left <= i:
        sum_ -= arr[left]
        left += 1

    maxLength = max(maxLength, i - left + 1)

print(maxLength)