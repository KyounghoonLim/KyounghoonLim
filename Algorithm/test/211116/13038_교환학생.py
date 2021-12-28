T = int(input().strip())

for tc in range(1, T+1):
    N = int(input().strip())
    test_case = list(map(int, input().strip().split()))

    cycle = 0
    for t in range(7):
        if test_case[t]:
            if not cycle:
                day = t
            cycle += 1

    ans, cls = 0, 0
    while cls + cycle < N:
        ans += 7
        cls += cycle

    for t2 in range(day, 7):
        ans += 1
        if test_case[t2]:
            cls += 1
            if cls == N:
                break

    print('#{} {}' .format(tc, ans))