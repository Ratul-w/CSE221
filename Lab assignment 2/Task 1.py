a = input().split()
N = int(a[0])
S = int(a[1])
arr = [int(x) for x in input().split()]
left = 0
right = N - 1

while left < right:
    sum_ = arr[left] + arr[right]
    if sum_ == S:
        print(f"{left + 1} {right + 1}")
        break
    elif sum_ < S:
        left += 1
    else:
        right -= 1
else:
    print("-1")