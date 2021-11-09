import sys
sys.setrecursionlimit(10000000)


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]


def apt(y, x):
    global cabbage

    for t in range(4):
        ti = y + di[t]
        tj = x + dj[t]
        if 0 <= ti < N and 0 <= tj < M:
            if not visited[ti][tj] and test_case[ti][tj] == 1:
                visited[ti][tj] = 1
                cabbage += 1
                Q.append([ti, tj])
    if Q:
        go = Q.pop(0)
        apt(go[0], go[1])

    return


T = int(input().strip())

for tc in range(1, T+1):
    M, N, K = map(int, input().strip().split())
    temp = [list(map(int, input().strip().split())) for _ in range(K)]
    test_case = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    for idx in temp:
        test_case[idx[1]][idx[0]] = 1
    ans = []
    for i in range(N):
        for j in range(M):
            if test_case[i][j] == 1 and not visited[i][j]:
                Q = []
                cabbage = 0
                apt(i, j)
                ans.append(cabbage)

    print(len(ans))