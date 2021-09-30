def calculate(lst, N_boxes, k_height, T1, T2, count, i, do="T1"):
    if do == "T1":
        T1 += n_list[i]
    else:
        T2 += n_list[i]
    # print(T1, T2)
    if T1 >= k_height and T2 >= k_height:
        return [count + 1, True]
    elif i == N_boxes - 1:
        return [-1, False]

    if T1 >= k_height:
        result_2 = calculate(lst, N_boxes, k_height, T1, T2, count + 1, i + 1, "T2")
        # print("result_2", result_2)
        # print("count", count)
        return result_2
    elif T2 >= k_height:
        result_1 = calculate(lst, N_boxes, k_height, T1, T2, count + 1, i + 1, "T1")
        # print("result_1", result_1)
        # print("count", count)
        return result_1
    else:
        result_1 = calculate(lst, N_boxes, k_height, T1, T2, count + 1, i + 1, "T1")
        result_2 = calculate(lst, N_boxes, k_height, T1, T2, count + 1, i + 1, "T2")

        # print("result_1", result_1)
        # print("result_2", result_2)
        # print("count", count)

        if result_1[1] and result_2[1]:
            return [min(result_1[0], result_2[0]), True]
        elif result_1[1] or result_2[1]:
            return [max(result_1[0], result_2[0]), True]
        else:
            return [-1, False]


T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    n_list = list(map(int, input().split()))
    if sum(n_list) < 2 * K:
        print(-1)
    else:
        n_list.sort(reverse=True)
        res_1 = calculate(n_list, N, K, 0, 0, 0, 0, "T1")
        res_2 = calculate(n_list, N, K, 0, 0, 0, 0, "T2")
        if res_1[1] and res_2[1]:
            print(min(res_1[0], res_2[0]))
        elif res_1[1]:
            print(res_1[0])
        elif res_2[1]:
            print(res_2[0])
        else:
            print(-1)
