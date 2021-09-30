import math

T = int(input())
for tc in range(T):
    N, D = map(int, input().split())
    ages = list(map(int, input().split()))
    risky = 0
    notrisky = 0
    for age in ages:
        if age >= 80 or age <= 9:
            risky += 1
        else:
            notrisky += 1
    print(math.ceil(risky / D) + math.ceil(notrisky / D))