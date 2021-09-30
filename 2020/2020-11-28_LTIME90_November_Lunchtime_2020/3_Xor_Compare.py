T = int(input())
for tc in range(T):
    X, Y, N = map(int, input().split())
    count = 0
    for Z in range(N + 1):
        if (X - Y) ^ Z < 0:
            count += 1
    print(count)