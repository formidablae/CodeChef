import math

N = int(input())
count = 0
for i in range(1, N + 1):
    for j in range(i + 1, N + 1):
        if i + 1 == j or i + math.gcd(i * j + i, i * j + j) == j:
            count += 1
print(count)
