c = input()
n = int(c, 16)
for i in range(1, 16):
    print(c + '*' + '%X' % i + '=' + '%X' % (i * n))
