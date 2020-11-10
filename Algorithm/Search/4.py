# 부품 찾기 (이진 탐색)
import sys

N = int(input())
array = list(map(int, sys.stdin.readline().rstrip().split()))
array.sort()
M = int(input())
targets = list(map(int, sys.stdin.readline().rstrip().split()))


def binary_search(array, target, start, end):
    if start > end:
        return "no"
    mid = (start + end) // 2
    if array[mid] == target:
        return "yes"
    elif array[mid] < target:
        return binary_search(array, target, mid + 1, end)
    else:
        return binary_search(array, target, start, mid - 1)


answer = []
for i in range(M):
    answer.append(binary_search(array, targets[i], 0, N - 1))

print(answer)
