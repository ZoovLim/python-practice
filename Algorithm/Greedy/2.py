N, M, K = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)
ans = 0

for i in range(M):
    if (i + 1) % K == 0:
        ans += a[1]
    else:
        ans += a[0]

print(ans)
