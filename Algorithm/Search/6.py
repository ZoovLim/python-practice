# 부품 탐색 (집합)
import sys

N = int(input())
array = set(map(int, sys.stdin.readline().rstrip().split()))
M = int(input())
targets = list(map(int, sys.stdin.readline().rstrip().split()))
answer = []

for i in targets:
    if i in array:
        answer.append("yes")
    else:
        answer.append("no")

print(answer)
