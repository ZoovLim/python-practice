n = int(input())
data = list(map(int, input().split()))
ans = [0] * 23
for i in data:
    ans[i - 1] += 1
for i in ans:
    print(i, end=' ')
