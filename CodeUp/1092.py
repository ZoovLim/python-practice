import math

ans = 1
a, b, c = map(int, input().split())
ans = (a * b) // math.gcd(a, b)
ans = (ans * c) // math.gcd(ans, c)
print(ans)
