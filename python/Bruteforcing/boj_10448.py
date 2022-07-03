###유레카이론
def ps_10448():
    from itertools import combinations_with_replacement

    t = int(input())

    # 삼각수
    tn = []
    for i in range(1,45):
        tn.append(i*(i+1)//2)

    # 삼각수 조합 값(3개 합)
    combi = list(combinations_with_replacement(tn, 3))
    total = []
    for case in combi:
        total.append(sum(case))

    for i in range(t):
        k = int(input())
        tf = True
        for case in total:
            if case == k:
                print(1)
                tf = False
                break
        # 없는 경우
        if tf:
            print(0)
