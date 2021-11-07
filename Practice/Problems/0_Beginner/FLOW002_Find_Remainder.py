T = int(input())
for case in range(T):
    A_and_B = list(map(int, input().split(" ")))
    print(A_and_B[0] % A_and_B[1])
