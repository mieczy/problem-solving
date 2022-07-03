###적어도 대부분의 배수
def ps_1145():
    num = list(map(int, input().split()))
    n = min(num)  # 가장 작은 n부터 확인

    while True:
        count = 0
        for i in num:
            # n이 입력한 값으로 나눠지는지 확인
            if n%i == 0:
                count += 1
        if count > 2:
            print(n)
            break
        n += 1
