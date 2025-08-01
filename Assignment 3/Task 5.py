def mod_pow(a, b, mod):
    result = 1
    a %= mod
    while b > 0:
        if b & 1:
            result = (result * a) % mod
        a = (a * a) % mod
        b >>= 1
    return result


def geometric_series_sum(a, n, m):
    if a == 1:
        return n % m
    mod_val = m * (a - 1)
    a_n_p = mod_pow(a, n + 1, mod_val)
    numerator = (a_n_p - a) % mod_val
    return (numerator // (a - 1)) % m


T = int(input())
lst = []
for _ in range(T):
    a, n, m = map(int, input().split())
    lst.append(geometric_series_sum(a, n, m))

print('\n'.join(map(str, lst)))