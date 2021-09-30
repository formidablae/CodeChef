T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    marked = []
    Xs = []
    Ys = []
    for mc in range(M):
        X, Y = map(int, input().split())
        Xs.append(X)
        Ys.append(X)
        marked.append([X, Y])
    if len(marked) <= 2:
        print(1, 2)
    else:
        i = 0
        ans = []
        startpointX = -1
        startpointY = -1
        direction = ""
        while i < M:
            if Xs.count(marked[i][0]) == 1:
                startpointX = i
                direction = "UPDOWN"
                break
            elif Ys.count(marked[i][1]) == 1:
                startpointY = i
                direction = "RIGHTLEFT"
                break

            print(direction)
            i += 1
        ans.append(max(startpointX, startpointY) + 1)

        lastpoint = marked[ans[0] - 1]
        marked.pop(0)
        while len(ans) < M:
            print(direction)
            print(marked)
            print(ans)
            if direction == "UPDOWN":
                index = Ys.index(lastpoint[1])
                ans.append(index + 1)
                marked.pop(index)
                direction = "RIGHTLEFT"
            elif direction == "RIGHTLEFT":
                index = Xs.index(lastpoint[0])
                ans.append(index + 1)
                marked.pop(index)
                direction = "UPDOWN"
        print(*ans)