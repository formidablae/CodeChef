T = int(input())
for tc in range(T):
    X, Y, Z = map(int, input().split())
    if Y <= 2 * Z + X:
        print("YES")
    else:
        print("NO")
