di = [0, 1]
dj = [1, 0]

def chess(y=0, x=0):
    global ans

    drawing = 0
    for i in range(y, y+7):
        for j in range(x, x+7):
            for k in range(2):
                if i + di[k] < N and test_case[i][j] == test_case[i+di[k]][j]:
                    if test_case[i+di[k]][j] == 'W':
                        test_case[i+di[k]][j] = 'B'
                    else:
                        test_case[i+di[k]][j] = 'W'
                    drawing += 1
                if j + dj[k] < M and test_case[i][j] == test_case[i][j+dj[k]]:
                    if test_case[i][j+dj[k]] == 'W':
                        test_case[i][j+dj[k]] = 'B'
                    else:
                        test_case[i][j+dj[k]] = 'W'
                    drawing += 1

    if drawing:
        if ans > drawing:
            ans = drawing
    if x + 7 == M and y + 7 == N:
        return
    x += 1
    if x + 7 == M and y + 7 != N:
        x = 0
        y += 1

    chess(y, x)


N, M = map(int, input().strip().split())

test_case = [input().strip() for _ in range(N)]
ans = 99999
chess()

print(ans)