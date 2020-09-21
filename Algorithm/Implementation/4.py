N, M = map(int, input().split())
row, col, look = map(int, input().split())
data = list()

for i in range(N):
    data.append(list(map(int, input().split())))

check = [(-1, 0), (0, -1), (1, 0), (0, 1)]
direction = [0, 3, 2, 1]
backStep = [(1, 0), (0, -1), (-1, 0), (0, 1)]
flag = True
answer = 0

while flag:
    flag = False
    data[row][col] = 2
    for i in range(1, 5):
        next_row = row + check[(look + i) % 4][0]
        next_col = col + check[(look + i) % 4][1]
        if 0 <= next_row < N and 0 <= next_col < M:
            if data[next_row][next_col] == 0:
                row = next_row
                col = next_col
                look = direction[(look + i) % 4]
                flag = True
                answer += 1
                break
    if flag is False:
        next_row = row + backStep[look][0]
        next_col = row + backStep[look][1]
        if data[next_row][next_col] == 2:
            row = next_row
            col = next_col
            flag = True
            answer += 1
        else:
            break

print(answer)
