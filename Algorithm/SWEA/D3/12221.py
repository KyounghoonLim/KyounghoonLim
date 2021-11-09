T = int(input().strip())

for tc in range(1, T+1):
    test_case = list(map(int, input().strip().split()))
    ans, flag = 1, 1
    for num in test_case:
        if ans // 10 or num // 10:
            print('#{} -1' .format(tc))
            flag = 0
            break
        else:
            ans *= num
    if flag:
        print('#{} {}' .format(tc, ans))