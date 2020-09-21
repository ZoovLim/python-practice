def solution(n):
    answer = []
    data = [[0] * n for _ in range(n)]
    count = 1
    row_start = 0
    row_end = n
    col_start = 0
    col_end = n

    while count <= n * (n + 1) / 2:
        for i in range(row_start, row_end):
            data[i][col_start] = count
            count += 1
        row_start += 2
        row_end -= 1
        for i in range(col_start + 1, col_end):
            data[row_end][i] = count
            count += 1
        for i in range(1, col_end - col_start - 1):
            data[row_end - i][col_end - 1 - i] = count
            count += 1
        col_start += 1
        col_end -= 2

    for d_list in data:
        for d in d_list:
            if d != 0:
                answer.append(d)

    return answer
