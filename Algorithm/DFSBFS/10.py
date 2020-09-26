N, M = map(int, input().split())
graph = []

for i in range(N):
    graph.append(list(map(int, input())))


def dfs(x, y):
    if x < 0 or x >= M or y < 0 or y >= N:
        return False
    if graph[y][x] == 0:
        graph[y][x] = 1
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False


result = 0
for i in range(N):
    for j in range(M):
        if dfs(j, i):
            result += 1

print(result)
