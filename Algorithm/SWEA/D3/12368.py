T = int(input().strip())

for tc in range(1, T+1):
    test_case = list(map(int, input().strip().split()))
    ans = 0
    for time in test_case:
        ans += time
        ans %= 24

    print('#{} {}' .format(tc, ans))