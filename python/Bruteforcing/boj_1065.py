###한수
def ps_1065():
    n = int(input())

    #100 미만의 수는 모두 한수: 공차 0
    if n < 100:
        print(n)      
    #세자리 수 한수 판별
    else:
        count = 99
        for i in range(100, n+1):
            #1000은 한수가 아니므로 제외
            if i == 1000:
                break
            n1, n10, n100 = map(int, str(i))
            if n10-n1 == n100-n10:
                count += 1

        print(count)
