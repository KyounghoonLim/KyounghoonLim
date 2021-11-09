di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]


def apt(y, x):
    global apartments

    for t in range(4):
        ti = y + di[t]
        tj = x + dj[t]
        if 0 <= ti < N and 0 <= tj < N:
            if not visited[ti][tj] and test_case[ti][tj] == '1':
                visited[ti][tj] = 1
                apartments += 1
                Q.append([ti, tj])
    if Q:
        go = Q.pop(0)
        apt(go[0], go[1])

    return


N = int(input().strip())
test_case = [input().strip() for _ in range(N)]
visited = [[0] * N for _ in range(N)]
ans = []
for i in range(N):
    for j in range(N):
        if test_case[i][j] == '1' and not visited[i][j]:
            Q = []
            apartments = 0
            apt(i, j)
            ans.append(apartments)
ans.sort()
print(len(ans))
for i in range(len(ans)):
    print(ans[i])