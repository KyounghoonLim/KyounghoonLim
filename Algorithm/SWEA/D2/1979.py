T = int(input().strip())

for tc in range(1, T + 1):
    N, K = map(int, input().strip().split())
    test_case = [list(map(int, input().strip().split())) for _ in range(N)]

    ans = 0
    for i in range(N):
        cnt_i = 0
        cnt_j = 0
        for j in range(N):
            if test_case[i][j]:
                cnt_i += 1
            else:
                if cnt_i == K:
                    ans += 1
                cnt_i = 0
            if test_case[j][i]:
                cnt_j += 1
            else:
                if cnt_j == K:
                    ans += 1
                cnt_j = 0
        if cnt_i == K:
            ans += 1
        if cnt_j == K:
            ans += 1

    print('#{} {}' .format(tc, ans))

