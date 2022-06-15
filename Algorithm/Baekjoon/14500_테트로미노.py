di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def tetromino(i, j, s, n=0):
    global ans

    if n == 3:
        if ans < s:
            ans = s
        return

    ### 이외의 경우 ###
    for t in range(4):
        ti, tj = i + di[t], j + dj[t]
        if 0 <= ti < N and 0 <= tj < M and not visited[ti][tj]:
            visited[ti][tj] = 1
            tetromino(ti, tj, s + test_case[ti][tj], n + 1)
            visited[ti][tj] = 0


N, M = list(map(int, input().split()))
test_case = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
ans = 0

for i in range(N):
    for j in range(M):
        visited[i][j] = 1

        ### ㅗ 모양일 경우 ###
        if (i, j) != (0, 0) and (i, j) != (0, M - 1) and (i, j) != (N - 1, 0) and (i, j) != (N - 1, M - 1):
            blocks = []
            ### 주변 블록들 집계 ###
            for t in range(4):
                ti, tj = i + di[t], j + dj[t]
                if 0 <= ti < N and 0 <= tj < M:
                    blocks.append(test_case[ti][tj])
            blocks.sort(reverse=True)
            sigma = test_case[i][j] + blocks[0] + blocks[1] + blocks[2]
            if ans < sigma:
                ans = sigma

        tetromino(i, j, test_case[i][j])
        visited[i][j] = 0

print(ans)