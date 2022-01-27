import copy

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def diffusion(arr):
    stack = []
    clean = 0

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 2:
                stack.append([i, j])
    while stack:
        v = stack.pop()
        for t in range(4):
            ti, tj = v[0] + di[t], v[1] + dj[t]
            if 0 <= ti < N and 0 <= tj < M and not arr[ti][tj]:
                stack.append([ti, tj])
                arr[ti][tj] = 2

    for i in range(N):
        for j in range(M):
            if not arr[i][j]:
                clean += 1

    return clean


def iso(arr, wall, w=3):
    global ans

    if not w:
        _arr = []
        for i in range(N):
            temp = [0] * M
            for j in range(M):
                temp[j] = arr[i][j]
            _arr.append(temp)
        result = diffusion(_arr)

        if ans < result:
            ans = result
        return

    for i in range(N):
        if wall and wall[-1][0] > i:
            continue
        for j in range(M):
            if wall and i == wall[-1] and j < wall[-1][1]:
                continue
            if not arr[i][j]:
                arr[i][j] = 1
                wall.append([i, j])
                iso(arr, wall, w-1)
                temp = wall.pop()
                arr[temp[0]][temp[1]] = 0


N, M = map(int, input().strip().split())

test_case = [list(map(int, input().strip().split())) for _ in range(N)]
ans = 0
iso(copy.deepcopy(test_case), [])

print(ans)