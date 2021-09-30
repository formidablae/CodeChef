T = int(input())
for tc in range(T):
    x, y = map(int, input().split())
    if (x + y) % 2 == 0:
        print("YES")
    else:
        print("NO")
