T = int(input().strip())

for tc in range(1, T+1):
    test_case = int(input().strip())
    ans = [0] * 5
    while test_case > 1:
        if not test_case % 11:
            test_case //= 11
            ans[4] += 1
        elif not test_case % 7:
            test_case //= 7
            ans[3] += 1
        elif not test_case % 5:
            test_case //= 5
            ans[2] += 1
        elif not test_case % 3:
            test_case //= 3
            ans[1] += 1
        elif not test_case % 2:
            test_case //= 2
            ans[0] += 1
    for t in range(5):
        ans[t] = str(ans[t])

    print('#{} {}' .format(tc, ' '.join(ans)))