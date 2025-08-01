MOD = 10 ** 9 + 7


def mat_mult(A, B):
    return [
        [(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % MOD,
         (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % MOD],
        [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % MOD,
         (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % MOD]
    ]


def mat_pow(A, X):
    result = [[1, 0], [0, 1]]

    base = A

    while X > 0:
        if X % 2 == 1:
            result = mat_mult(result, base)
        base = mat_mult(base, base)
        X = X // 2

    return result


T = int(input())

for k in range(T):
    a11, a12, a21, a22 = [int(x) for x in input().split()]
    A = [[a11, a12], [a21, a22]]

    X = int(input())

    result = mat_pow(A, X)

    for i in range(2):
        print(result[i][0], result[i][1])