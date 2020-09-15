arr = [[0] * 19 for _ in range(19)]
for i in range(19):
    t = list(map(int, input().split()))
    for j in range(19):
        arr[i][j] = t[j]
n = int(input())
data = [[0] * 2 for _ in range(n)]
for i in range(n):
    x, y = map(int, input().split())
    data[i][0] = x
    data[i][1] = y
for d in data:
    x = d[0] - 1
    y = d[1] - 1
    for i in range(19):
        if arr[x][i] == 0:
            arr[x][i] = 1
        else:
            arr[x][i] = 0
    for i in range(19):
        if arr[i][y] == 0:
            arr[i][y] = 1
        else:
            arr[i][y] = 0
for i in range(19):
    for j in range(19):
        print(arr[i][j], end=' ')
    print()
