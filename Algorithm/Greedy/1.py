# 거스름돈
N = int(input())
ans = 0
coins = [500, 100, 50, 10]
for coin in coins:
    ans += N // coin
    N %= coin
print(ans)
