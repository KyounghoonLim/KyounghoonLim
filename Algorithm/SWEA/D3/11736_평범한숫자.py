T = int(input().strip())

for tc in range(1, T+1):
    N = int(input().strip())
    test_case = list(map(int, input().strip().split()))

    ans = 0
    for t in range(1, N-1):
        if test_case[t-1] < test_case[t] < test_case[t+1] or\
            test_case[t+1] < test_case[t] < test_case[t-1]:
            ans += 1

    print('#{} {}' .format(tc, ans))