data = list(map(int, input().split('.')))
print('%02d' % data[2] + '-' + '%02d' % data[1] + '-' + '%04d' % data[0])
