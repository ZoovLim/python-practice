data = []
for i in range(10):
    tmp = list(map(int, input().split()))
    data.append(tmp)

x = 1
y = 1
if data[x][y] == 2:
    data[x][y] = 9
else:
    data[x][y] = 9
    while True:
        if y < 19 and data[x][y + 1] != 1:
            if data[x][y + 1] == 2:
                data[x][y + 1] = 9
                break
            data[x][y + 1] = 9
            y += 1
        elif x < 19 and data[x + 1][y] != 1:
            if data[x + 1][y] == 2:
                data[x + 1][y] = 9
                break
            data[x + 1][y] = 9
            x += 1
        else:
            break

for i in range(10):
    for j in range(10):
        print(data[i][j], end=' ')
    print()
