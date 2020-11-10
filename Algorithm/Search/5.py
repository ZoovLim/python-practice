# 부품 찾기 (계수 정렬)
N = int(input())
array = [0] * 1000001
for i in input().split():
    array[int(i)] = 1

M = int(input())
targets = list(map(int, input().split()))
answer = []

for i in range(len(targets)):
    if array[targets[i]] == 1:
        answer.append("yes")
    else:
        answer.append("no")

print(answer)
