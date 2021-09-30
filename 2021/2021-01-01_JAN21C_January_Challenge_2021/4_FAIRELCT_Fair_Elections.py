T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    jackson_list = list(map(int, input().split()))
    johnson_list = list(map(int, input().split()))
    jackson_list.sort(reverse=False)
    johnson_list.sort(reverse=True)
    votes_jackson = sum(jackson_list)
    votes_johnson = sum(johnson_list)
    if votes_jackson > votes_johnson:
        print(0)
    else:
        count = 0
        i = 0
        flag = False
        while i < min(N, M):
            diff = johnson_list[i] - jackson_list[i]
            if diff <= 0:
                break
            votes_jackson += diff
            votes_johnson -= diff
            count += 1
            if votes_jackson > votes_johnson:
                flag = True
                break
            i += 1
        if flag:
            print(count)
        else:
            print(-1)
