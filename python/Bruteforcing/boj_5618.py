###공약수
def ps_5618():
    n = int(input())
    num = list(map(int, input().split()))
    min_n = min(num)
    result = []

    for i in range(1, min_n+1):
        # n=2인 경우
        if len(num) == 2:
            if num[0]%i==0 and num[1]%i==0:
                result.append(i)
        # n=3인 경우
        else:
            if num[0]%i==0 and num[1]%i==0 and num[2]%i==0:
                result.append(i)

    for n in result:
        print(n)
