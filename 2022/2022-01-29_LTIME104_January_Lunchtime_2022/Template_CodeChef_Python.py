T = int(input())
for tc in range(T):
    N = int(input())
    A, B = map(int, input().split())
    f_list = list(map(int, input().split()))
    if len(f_list) == 0:
        print(1)
    else:
        print(N, A, B, f_list)