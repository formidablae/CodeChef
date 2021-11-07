T = int(input())
for tc in range(T):
    n = int(input())
    sumofdig = 0
    while n:
        sumofdig, n = sumofdig + n % 10, n // 10
    print(sumofdig)
