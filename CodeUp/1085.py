h, b, c, s = map(int, input().split())
ans = h * b * c * s / (2 ** 23)
print('%.1f' % ans + ' MB')
