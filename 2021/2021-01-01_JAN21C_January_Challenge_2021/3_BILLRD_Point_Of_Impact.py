T = int(input())
for tc in range(T):
    N, K, x, y = map(int, input().split())
    if x == y:
        print(N, N)
    else:
        right_x, right_y = N, N - (max(x, y) - min(x, y))
        left_x, left_y = 0, N - right_y
        top_x, top_y = right_y, N
        bottom_x, bottom_y = N - right_y, 0
        rotat = K % 4
        if x > y:
            if rotat == 1:
                print(right_x, right_y)
            elif rotat == 2:
                print(top_x, top_y)
            elif rotat == 3:
                print(left_x, left_y)
            else:
                print(bottom_x, bottom_y)
        else:
            if rotat == 1:
                print(top_x, top_y)
            elif rotat == 2:
                print(right_x, right_y)
            elif rotat == 3:
                print(bottom_x, bottom_y)
            else:
                print(left_x, left_y)
