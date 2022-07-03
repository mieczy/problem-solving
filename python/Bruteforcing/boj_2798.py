###블랙잭
def ps_2798():
    from itertools import combinations

    N, M = map(int, input().split())
    card = list(map(int, input().split()))

    total = 0

    ### N<=100일때, 최대 161700개 조합
    for case in combinations(card, 3):
        temp = sum(case)
        if total <= temp <= M:
            total = temp

    print(total)
