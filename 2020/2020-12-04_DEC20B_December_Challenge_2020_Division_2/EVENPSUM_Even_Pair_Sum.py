import math

T = int(input())
for tc in range(T):
    A, B = map(int, input().split())
    all_even_A = math.floor(A / 2)
    all_even_B = math.floor(B / 2)
    all_odds_A = math.ceil(A / 2)
    all_odds_B = math.ceil(B / 2)
    print(all_even_A * all_even_B + all_odds_A * all_odds_B)