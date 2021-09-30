# def checkflag(matrix, n_dim, m_dim):
#     flag_bool = True
#     i = 0
#     if m_dim > n_dim:
#         while i < M - N:
#             diag = matrix[0][i]
#             j = 1
#             while i + j < M and j < N:
#                 if diag != matrix[j][i + j]:
#                     flag_bool = False
#                     break
#                 # print("i =", i, "j =", j, m_matrix[j][i + j])
#                 j += 1
#             if not flag_bool:
#                 break
#             i += 1
#     else:
#         while i < N - M:
#             diag = matrix[i][0]
#             j = 1
#             while i + j < N and j < M:
#                 if diag != matrix[i + j][j]:
#                     flag_bool = False
#                     break
#                 # print("i =", i, "j =", j, m_matrix[i + j][j])
#                 j += 1
#             if not flag_bool:
#                 break
#             i += 1
#     return flag_bool
#
#
# T = int(input())
# for tc in range(T):
#     N, M = map(int, input().split())
#     m_matrix = []
#     for nn in range(N):
#         A, B, C = map(int, input().split())
#         m_matrix.append([A, B, C])
#         # print([A, B, C])
#     if M > N:
#         flag = checkflag(m_matrix, N, M)
#         Q = int(input())
#         for qq in range(Q):
#             X, Y, V = map(int, input().split())
#             # print([X, Y, V])
#             m_matrix[X - 1][Y - 1] = V
#             # print(m_matrix)
#             # print("i =", X - 1, "i + j =", Y - 1, "diag =", m_matrix[0][Y - X], "matrix el =", m_matrix[X - 1][Y - 1])
#             if Y - X < M - N:
#                 # print("enter if")
#                 if flag and (X - 1 != 0 or Y - X != Y - 1) and m_matrix[0][Y - X] == m_matrix[X - 1][Y - 1]:
#                     # print("enter if if")
#                     flag = True
#                     print("Yes")
#                 elif flag and m_matrix[N - 1][N - 1 + Y - X] == m_matrix[X - 1][Y - 1]:
#                     # print("enter if elif")
#                     flag = True
#                     print("Yes")
#                 else:
#                     # print("enter if else")
#                     flag = checkflag(m_matrix, N, M)
#                     if flag:
#                         print("Yes")
#                     else:
#                         print("No")
#             elif flag:
#                 # print("enter elif")
#                 print("Yes")
#             else:
#                 # print("enter else")
#                 print("No")
#     else:
#         flag = checkflag(m_matrix, N, M)
#         Q = int(input())
#         for qq in range(Q):
#             X, Y, V = map(int, input().split())
#             # print([X, Y, V])
#             m_matrix[X - 1][Y - 1] = V
#             # print(m_matrix)
#             # print("i =", X - 1, "i + j =", Y - 1, "diag =", m_matrix[0][Y - X], "matrix el =", m_matrix[X - 1][Y - 1])
#             if Y - X < M - N:
#                 # print("enter if")
#                 if flag and (X - 1 != 0 or Y - X != Y - 1) and m_matrix[0][Y - X] == m_matrix[X - 1][Y - 1]:
#                     # print("enter if if")
#                     flag = True
#                     print("Yes")
#                 elif flag and m_matrix[N - 1][N - 1 + Y - X] == m_matrix[X - 1][Y - 1]:
#                     # print("enter if elif")
#                     flag = True
#                     print("Yes")
#                 else:
#                     # print("enter if else")
#                     flag = checkflag(m_matrix, N, M)
#                     if flag:
#                         print("Yes")
#                     else:
#                         print("No")
#             elif flag:
#                 # print("enter elif")
#                 print("Yes")
#             else:
#                 # print("enter else")
#                 print("No")