T = int(input())
for tc in range(T):
    posPol, posThi, step, end = map(int, input().split())
    if abs(posThi - posPol) % ((step % 2) + 1) == 1:
        print("No")
    else:
        print("Yes")