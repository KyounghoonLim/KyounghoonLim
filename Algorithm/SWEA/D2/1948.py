def is_in(n):
    for m in sm:
        if n == m:
            return True

    return


T = int(input().strip())

for tc in range(1, T+1):
    test_case = list(map(int, input().strip().split()))
    sm = [4, 6, 9, 11]
    ans = 0
    for m in range(test_case[0], test_case[2]):
        if m == 2:
            ans += 28
        elif is_in(m):
            ans += 30
        else:
            ans += 31
    if test_case[3] - test_case[1] > 0:
        ans += test_case[3] - test_case[1]
    else:
        ans -= test_case[1] - test_case[3]

    print('#{} {}' .format(tc, ans+1))