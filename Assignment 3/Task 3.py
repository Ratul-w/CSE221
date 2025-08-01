a, b = [int(x) for x in input().split()]
mod = 107

a = a % mod
result = 1

while b > 0:
    if b % 2 == 1:
        result = (result * a) % mod
    a = (a * a) % mod
    b = b // 2

print(result)