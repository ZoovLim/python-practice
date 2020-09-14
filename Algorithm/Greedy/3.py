N, M = map(int, input().split())
ans = 0
for i in range(N):
    data = list(map(int, input().split()))
    ans = max(ans, min(data))

print(ans)
