# 피보나치 (Bottom-Up)
m = [0] * 101

m[1] = 1
m[2] = 1
n = 100

for i in range(3, n + 1):
    m[i] = m[i - 2] + m[i - 1]

print(m[n])
