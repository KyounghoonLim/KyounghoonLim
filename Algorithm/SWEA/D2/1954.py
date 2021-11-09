di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

T = int(input().strip())

for tc in range(1, T + 1):
    N = int(input().strip())
    temp = [[0] * N for _ in range(N)]

    cnt = 1
    i, j = 0, 0
    while True:
        temp[i][j] = cnt
        if cnt == N * N:
            break
        for t in range(4):
            ti = i + di[t]
            tj = j + dj[t]
            if 0 <= ti < N and 0 <= tj < N:
                if temp[ti][tj] == 0:
                    i = ti
                    j = tj
                    cnt += 1
                    break

    print('#{} ' .format(tc))
    for t1 in range(N):
        for t2 in range(N):
            print(temp[t1][t2], end=' ')
        print()