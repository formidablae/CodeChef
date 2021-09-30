T = int(input())
for tc in range(T):
    N = int(input())
    lines = []
    for r in range(N):
        row_list = list(map(int, input().split()))
        M = row_list[0]
        points = row_list[1: M + 1]
        lines.append(points)
    collis = 0
    for line in lines:
        # ln.sort()
        negat = len(list(filter(lambda x: (x < 0), line)))
        posit = len(line) - negat
        collis += negat * posit
    print(collis)

