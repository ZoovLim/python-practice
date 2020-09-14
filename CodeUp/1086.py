w, h, b = map(int, input().split())
ans = w * h * b / (2 ** 23)
print('%.2f' % ans + ' MB')
