T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    n_list = list(map(int, input().split()))
    if K == 1 or sum(n_list) % K == 0:
        print(0)
    else:
        print(1)
