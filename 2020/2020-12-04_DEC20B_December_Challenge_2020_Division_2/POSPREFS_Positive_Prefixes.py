T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    if K == N:
        print(*list(range(1, N + 1)))
    else:
        seq = []
        negatives = 0
        positives = 0
        for i in range(1, N + 1):
            if negatives < N - K and positives < K and (i - 1) % 2 == 0:
                seq.append(-i)
                negatives += 1
            elif negatives < N - K and positives < K:
                seq.append(i)
                positives += 1
            elif negatives < N - K:
                seq.append(-i)
                negatives += 1
            else:
                seq.append(i)
        print(*seq)