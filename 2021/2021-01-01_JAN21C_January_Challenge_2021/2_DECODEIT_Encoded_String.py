T = int(input())
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for tc in range(T):
    N = int(input())
    S = input()
    decoded = ""
    for i in range(0, N, 4):
        decoded += alpha[int(S[i:i+4], 2)]
    print(decoded)