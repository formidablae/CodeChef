from collections import deque
import math


def distance_travable(N_cars, f_list_fuel):
    distance = 0
    if len(f_list_fuel) == 1:
        return f_list_fuel[0]
    else:
        index = 1
        while f_list[0] > 0 and index < N_cars:
            if f_list_fuel[index] > 0:
                f_list_fuel[0] += f_list_fuel[index]
                f_list_fuel[index] = 0
            index += 1
            f_list_fuel[0] -= 1
            distance += 1
        distance += f_list[0]
        return distance


T = int(input())
for tc in range(T):
    N = int(input())
    f_list = list(map(int, input().split()))
    c_list = list(map(int, input().split()))
    if len(f_list) == 1:
        print(f_list[0] * c_list[0])
    else:
        cost = []
        products = []
        for i in range(N):
            products.append(f_list[i] * c_list[i])
        f_copy = f_list.copy()
        for j in range(N):
            distance_trav = distance_travable(N, f_copy)
            if distance_trav >= N:
                cost.append(f_list[j] * c_list[j])
            f_copy.append(f_copy.pop(0))
        print(min(cost))