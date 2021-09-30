# T = int(input())
# for tc in range(T):
#     N_sorcerers, M_spells = map(int, input().split())
#     spells_list = list(map(int, input().split()))
#     kills = 0
#     if M_spells == 1 and spells_list[0] <= N_sorcerers:
#         if spells_list[0] < N_sorcerers and N_sorcerers > 1:
#             kills = N_sorcerers - spells_list[0]
#     else:
#         i = 0
#         while i < M_spells:
#             # if N_sorcerers == 1:
#             #     break
#             # if spells_list[i] % N_sorcerers != 0:
#             #     newkills = N_sorcerers - spells_list[i] % N_sorcerers
#             #     N_sorcerers -= newkills
#             #     kills += newkills
#             #     i = 0
#             if spells_list[i] % N_sorcerers != 0:
#                 N_sorcerers -= 1
#                 kills += 1
#                 i = 0
#             else:
#                 i += 1
#     print(kills)