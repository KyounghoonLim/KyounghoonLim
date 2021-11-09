def eff(i, j, d):
    for td in range(d):
        td += 1
        for t in range(4):
            ti = i + di[t] * td
            tj = j + dj[t] * td
            if 0 <= ti < N and 0 <= tj < N:
                if test_case[ti][tj] == 'H':
                    test_case[ti][tj] = 'E'


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

T = int(input().strip())

for tc in range(1, T+1):
    N = int(input().strip())
    test_case = [list(input().strip()) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if test_case[i][j] == 'A':
                eff(i, j, 1)
            elif test_case[i][j] == 'B':
                eff(i, j, 2)
            elif test_case[i][j] == 'C':
                eff(i, j, 3)
    cnt = 0
    for t_i in range(N):
        for t_j in range(N):
            if test_case[t_i][t_j] == 'H':
                cnt += 1

    print('#{} {}' .format(tc, cnt))