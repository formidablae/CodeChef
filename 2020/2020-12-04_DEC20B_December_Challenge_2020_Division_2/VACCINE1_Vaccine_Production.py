import math

D1, V1, D2, V2, P = map(int, input().split())
if P == 1:
    print(min(D1, D2))
else:
    if D1 < D2 and V1 * (D2 - D1) >= P:
        print(D1 - 1 + math.ceil(P / V1))
    elif D1 >= D2 and V2 * (D1 - D2) >= P:
        print(D2 - 1 + math.ceil(P / V2))
    else:
        if D1 < D2:
            print(D2 - 1 + math.ceil((P - V1 * (D2 - D1)) / (V1 + V2)))
        else:
            print(D1 - 1 + math.ceil((P - V2 * (D1 - D2)) / (V1 + V2)))
