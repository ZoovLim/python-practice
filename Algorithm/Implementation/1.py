N = int(input())
data = input().split()
x, y = 1, 1

for d in data:
    if d == 'L' and x > 1:
        x -= 1
    elif d == 'R' and x < N:
        x += 1
    elif d == 'U' and y > 1:
        y -= 1
    elif d == 'D' and y < N:
        y += 1
    else:
        continue

print(y, x)
