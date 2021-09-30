T = int(input())
for tc in range(T):
    N = int(input())
    f_list = list(map(int, input().split()))
    distance = 0
    if len(f_list) == 1:
        print(f_list[0])
    else:
        i = 1
        while f_list[0] > 0 and i < N:
            if f_list[i] > 0:
                f_list[0] += f_list[i]
                f_list[i] = 0
            i += 1
            f_list[0] -= 1
            distance += 1
        distance += f_list[0]
        print(distance)
