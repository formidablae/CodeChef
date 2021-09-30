# T = int(input())
# for tc in range(T):
#     S_list = list(input())
#     # S_list = ["a", "a", "b", "a", "a"]
#     count_letters = {}
#     single_letters = 0
#     for ch in S_list:
#         count_letters[ch] = S_list.count(ch)
#         if count_letters[ch] == 1:
#             single_letters += 1
#     count = 0
#     i = 0
#     keys_to_iter = list(count_letters.keys())
#     # print(single_letters)
#     # print(count_letters)
#     # print(keys_to_iter)
#     # print(len(keys_to_iter))
#     while i < len(keys_to_iter) and single_letters > 0:
#         # print(count_letters)
#         # print(single_letters)
#         if count_letters[keys_to_iter[i]] > 1:
#             count_letters[keys_to_iter[i]] = count_letters[keys_to_iter[i]] - 2
#             single_letters -= 1
#             count += 1
#         if count_letters[keys_to_iter[i]] == 1:
#             single_letters += 1
#             i += 1
#         elif count_letters[keys_to_iter[i]] < 1:
#             i += 1
#         # print(count_letters)
#         # print(single_letters)
#     print(count)