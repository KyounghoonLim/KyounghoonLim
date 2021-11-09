T = int(input().strip())

for tc in range(1, T+1):
    N = int(input().strip())
    test_case = [list(map(int, input().strip().split())) for _ in range(N)]
    v = 0
    d = 0
    for command in test_case:
        if command[0] == 1:
            v += command[1]
        elif command[0] == 2:
            v -= command[1]
        if v < 0:
            v = 0
        d += v

    print('#{} {}' .format(tc, d))