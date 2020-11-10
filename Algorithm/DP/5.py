# 개미 전사
N = int(input())
array = list(map(int, input().split()))
d = [0] * N

d[0] = array[0]
d[1] = array[1]

for i in range(2, N):
    d[i] = max(d[i - 2] + array[i], d[i - 1])

answer = max(d[N - 2], d[N - 1])
print(answer)
