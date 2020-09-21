pos = input()
row = int(pos[1])
col = int(ord(pos[0])) - ord('a') + 1
steps = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
answer = 0

for step in steps:
    tmp_row = row + step[0]
    tmp_col = col + step[1]
    if 1 <= tmp_row <= 8 and 1 <= tmp_col <= 8:
        answer += 1

print(answer)
