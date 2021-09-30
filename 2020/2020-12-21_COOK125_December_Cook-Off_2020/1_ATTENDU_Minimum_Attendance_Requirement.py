T = int(input())
for tc in range(T):
    N = int(input())
    attendance = list(map(int, input()))
    if sum(attendance) + 120 - N < 90:
        print("NO")
    else:
        print("YES")