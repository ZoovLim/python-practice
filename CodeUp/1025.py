n = input()
digit = 10000
for i in range(5):
    print('[' + str(int(n[i]) * digit) + ']')
    digit //= 10
