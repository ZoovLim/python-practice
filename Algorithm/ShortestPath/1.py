# 다익스트라 (방법 1 O(V^2))

import sys

INF = int(1e9)

# 노드 개수 : n, 간선 개수 : m 입력
n, m = map(int, sys.stdin.readline().rstrip().split())
start = int(input())

# 그래프 리스트 만들기
graph = [[] for i in range(n + 1)]

# 방문 리스트
visited = [False] * (n + 1)

# 최단 거리 테이블 초기화
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append((b, c))


# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드 번호 반환
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index


def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for i in graph[start]:
        distance[i[0]] = i[1]
    for i in range(n - 1):
        smallest = get_smallest_node()
        visited[smallest] = True
        for j in graph[smallest]:
            cost = distance[smallest] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost


dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
