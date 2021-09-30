# # cook your dish here
# T = int(input())
# for tc in range(T):
#     N = int(input())
#     S = list(input())
#     P = list(input())
#     lengS = len(S)
#     lengP = len(P)
#     i = 0
#     while i < len(S):
#         letter = S[i]
#         if letter == P[i]:
#             pass
#         else:
#             newletter = str((int(letter) + 1) % 2)
#             indexat = S[i:lengS].index(newletter)
#             if indexat < 0:
#                 print("No")
#                 break
#             S[i] = newletter
#             S[indexat] = letter
#         i += 1
#     if S == P:
#         print("Yes")