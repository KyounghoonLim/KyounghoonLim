di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def mountain(pos, moves, ring=0):
    global ans

    if ring > ans:
        return
    if test_case[pos[0]][pos[1]] == 3:
        if ring < ans:
            ans = ring
        return
    if moves:
        for t in range(4):
            i, j = pos[0] + di[t], pos[1] + dj[t]
            if (0 <= i < M and 0 <= j < N) and not visited[i][j]:
                visited[i][j] = True
                if test_case[i][j] == 1:
                    temp = ans
                    mountain((i, j), moves-1, ring)
                    if temp == ans:
                        mountain((i, j), L, ring+1)
                else:
                    mountain((i, j), moves - 1, ring)
                visited[i][j] = False


T = int(input().strip())

for tc in range(1, T+1):
    M, N, L = map(int, input().strip().split())
    test_case = [list(map(int, input().strip().split())) for _ in range(M)]
    for t in range(N):
        if test_case[M-1][t] == 2:
            st = (M-1, t)
        if test_case[0][t] == 3:
            ed = (0, t)
    min_distance = abs(st[0] - ed[0]) + abs(st[1] - ed[1])
    for ti in range(M):
        for tj in range(N):
            if test_case[ti][tj] == 1:
                distance = abs(ed[0] - ti) + abs(ed[1] - tj)
                if min_distance > distance:
                    min_distance = distance
    if min_distance > L:
        print('#{} -1' .format(tc))
        continue
    ans = 99999999
    visited = [[False] * N for _ in range(M)]
    mountain(st, L)
    if ans == 99999999:
        print('#{} -1' .format(tc))
    else:
        print('#{} {}' .format(tc, ans))