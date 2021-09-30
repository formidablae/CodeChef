T = int(input())
for tc in range(T):
    N, K, D = map(int, input().split())
    n_list = list(map(int, input().split()))
    print(min(sum(n_list) // K, D))