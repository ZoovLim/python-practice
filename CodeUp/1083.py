n = int(input())
s = ""
for i in range(1, n + 1):
    if i % 3 == 0:
        s += 'X '
    else:
        s += str(i) + ' '
print(s)
