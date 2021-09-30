N, M = map(int, input().split())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))
minA = min(A_list)
swaps = 0
for i in range(M):
    if B_list[i] < minA:
        swaps += N
print(swaps)