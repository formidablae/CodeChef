import math
from functools import reduce


def find_gcd(list):
    x = reduce(math.gcd, list)
    return x


def count_2_factor(n):
    count2 = 0
    while n % 2 == 0:
        count2 = count2 + 1
        n = n / 2
    return count2


T = int(input())
for tc in range(T):
    N = int(input())
    list_A = list(map(int, input().split()))
    minim_op = math.inf
    for el in list_A:
        this_factors = count_2_factor(el)
        if this_factors == 0:
            minim_op = this_factors
            break
        elif this_factors < minim_op:
            minim_op = this_factors
    print(minim_op)