# 경로 압축 기법 사용

# 서로소 집합 구현

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())
parent = [0] * (v + 1)

for i in range(1, v + 1):
    parent[i] = i

for i in range(e):
    a, b = map(int, input().split())
    union(parent, a, b)

for i in range(1, v + 1):
    print(i, ":", find(parent, i), end=", ")

print()

for i in range(1, v + 1):
    print(i, ":", parent[i], end=", ")
