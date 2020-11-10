# 효율적인 화폐 구성
N, M = list(map(int, input().split()))
coins = []

for i in range(N):
    coins.append(int(input()))

d = [10000] * (M + 1)
d[0] = 0

for i in range(1, M + 1):
    for j in coins:
        if i - j >= 0:
            d[i] = min(d[i], d[i - j] + 1)

if d[M] == 10000:
    print(-1)
else:
    print(d[M])
