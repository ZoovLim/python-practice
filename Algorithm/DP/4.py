# 1로 만들기
X = int(input())
d = [30000] * (X + 1)
d[1] = 0

for i in range(1, X + 1):
    if i + 1 <= X:
        d[i + 1] = min(d[i + 1], d[i] + 1)
    if 2 * i <= X:
        d[2 * i] = min(d[2 * i], d[i] + 1)
    if 3 * i <= X:
        d[3 * i] = min(d[3 * i], d[i] + 1)
    if 5 * i <= X:
        d[5 * i] = min(d[5 * i], d[i] + 1)

print(d[X])
