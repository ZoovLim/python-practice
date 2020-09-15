w, h = map(int, input().split())
n = int(input())
arr = [[0] * (h + 1) for _ in range(w + 1)]
data = []

for i in range(n):
    tmp = list(map(int, input().split()))
    data.append(tmp)

for i in data:
    length = i[0]
    d = i[1]
    x = i[2]
    y = i[3]
    for j in range(length):
        if d == 0:
            arr[x][y + j] = 1
        else:
            arr[x + j][y] = 1

for i in range(1, w + 1):
    for j in range(1, h + 1):
        print(arr[i][j], end=' ')
    print()
