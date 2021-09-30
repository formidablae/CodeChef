import math

t = int(input())
for tc in range(t):
    n, x = map(int, input().split())
    earn = 0
    if n < 3: earn = 0
    elif n == 3: earn = 2
    elif n == 4: earn = 4
    else:
        lengthOdds = 0
        lengthEvens = 0
        if n % 2 == 0: earn = n * (int(n / 2) - 1)
        else:
            lengthOdds = int((n - 1) / 2 + 1)
            lengthEvens = int((n - 1) / 2)
            earn = lengthOdds * (lengthOdds - 1) + lengthEvens * (lengthEvens - 1)
    if earn > x: print("{} Profit".format(earn - x))
    elif earn < x: print("{} Loss".format(x - earn))
    else: print("{} Null".format(0))
