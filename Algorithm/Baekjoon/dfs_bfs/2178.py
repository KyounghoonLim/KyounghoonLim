import sys
sys.setrecursionlimit(10000000)


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]


def maze(i=0, j=0, length=1):
    global ans

    if i == N-1 and j == M-1:
        if ans > length:
            ans = length

    for t in range(4):
        ti = i + di[t]
        tj = j + dj[t]
        if 0 <= ti < N and 0 <= tj < M:
            if not visited[ti][tj] and test_case[ti][tj] == '1':
                visited[ti][tj] = 1
                Q.append([ti, tj, length+1])
    if Q:
        go = Q.pop(0)
        maze(go[0], go[1], go[2])

    return


N, M = map(int, input().strip().split())
test_case = [input().strip() for _ in range(N)]
visited = [[0] * M for _ in range(N)]
Q = []
ans = 999999
maze()

print(ans)
