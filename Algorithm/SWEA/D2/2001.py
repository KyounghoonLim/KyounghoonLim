T = int(input().strip())

for tc in range(1, T + 1):
    test_case = []
    N, M = map(int, input().strip().split())
    for idx in range(N):
        test_case.append(list(map(int, input().strip().split())))

    kill_list = []
    for i in range(N - M + 1):
        temp = []
        for j in range(N):
            for k in range(M):
                temp.append(test_case[i + k][j])
                if len(temp) == M * M:
                    kills = 0
                    for l in temp:
                        kills += l
                    kill_list.append(kills)
                    for m in range(M):
                        temp.pop(0)

    maxi = kill_list[0]
    for n in kill_list:
        if n > maxi:
            maxi = n
    print('#{} {}'.format(tc, maxi))
