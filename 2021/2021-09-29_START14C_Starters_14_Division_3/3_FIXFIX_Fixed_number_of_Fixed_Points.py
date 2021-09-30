def shift(seq, n=0):
    a = n % len(seq)
    return seq[-a:] + seq[:-a]


T = int(input())
for tc in range(T):
    n, k = map(int, input().split())
    if n - k == 0:
        print(*list(range(1, n+1)), sep=" ")
    elif n - k > 1:
        result = list(range(1, k+1)) + shift(list(range(k+1, n+1)), 1)
        print(*result, sep=" ")
    else: # n - k == 1
        print("-1")
