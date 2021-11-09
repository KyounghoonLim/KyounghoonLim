import sys
sys.setrecursionlimit(10000000)


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]


def tomato(i=0, j=0, length=1):
    global ans

    for t in range(4):
        ti = i + di[t]
        tj = j + dj[t]
        if 0 <= ti < N and 0 <= tj < M:
            if not visited[ti][tj] and test_case[ti][tj] == '1':
                visited[ti][tj] = 1
                Q.append([ti, tj, length+1])
    if Q:
        go = Q.pop(0)
        tomato(go[0], go[1], go[2])

    return


M, N = map(int, input().strip().split())
test_case = [list(map(int, input().strip().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
Q = []
ans = 0

tomato()

print(ans)
