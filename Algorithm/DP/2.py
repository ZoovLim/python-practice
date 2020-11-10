# 피보나치 (메모이제이션, Top-Down)
m = [0] * 101


def fibo(x):
    if x == 1 or x == 2:
        return 1
    if m[x] != 0:
        return m[x]
    m[x] = fibo(x - 2) + fibo(x - 1)
    return m[x]


print(fibo(100))
