# 떡볶이 떡 만들기
import sys

N, M = list(map(int, input().split()))
array = list(map(int, sys.stdin.readline().rstrip().split()))

start = 0
end = max(array)
result = 0

while start <= end:
    mid = (start + end) // 2
    total = 0
    for i in array:
        if i > mid:
            total += (i - mid)
    if total == M:
        result = mid
        break
    elif total > M:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
