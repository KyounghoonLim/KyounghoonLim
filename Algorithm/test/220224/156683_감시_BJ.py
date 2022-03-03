import copy

def do(temp):
    if not temp:
        return '#'
    return temp

def cam1(arr, n, d):
    pos = camera[n]
    if d == 0:
        for j in range(pos[1], M):
            if arr[pos[0]][j] == 6:
                break
            arr[pos[0]][j] = do(arr[pos[0]][j])
    elif d == 1:
        for i in range(pos[0], N):
            if arr[i][pos[1]] == 6:
                break
            arr[i][pos[1]] = do(arr[i][pos[1]])
    elif d == 2:
        for j in range(pos[1], -1, -1):
            if arr[pos[0]][j] == 6:
                break
            arr[pos[0]][j] = do(arr[pos[0]][j])
    else:
        for i in range(pos[0], -1, -1):
            if arr[i][pos[1]] == 6:
                break
            arr[i][pos[1]] = do(arr[i][pos[1]])

    return arr


def cam2(arr, n, d):
    pos = camera[n]
    if d % 2 == 0:
        for j in range(pos[1], M):
            if arr[pos[0]][j] == 6:
                break
            arr[pos[0]][j] = do(arr[pos[0]][j])
        for j in range(pos[1], -1, -1):
            if arr[pos[0]][j] == 6:
                break
            arr[pos[0]][j] = do(arr[pos[0]][j])
    elif d % 2 == 1:
        for i in range(pos[0], N):
            if arr[i][pos[1]] == 6:
                break
            arr[i][pos[1]] = do(arr[i][pos[1]])
        for i in range(pos[0], -1, -1):
            if arr[i][pos[1]] == 6:
                break
            arr[i][pos[1]] = do(arr[i][pos[1]])

    return arr


def cam3(arr, n, d):
    pos = camera[n]
    if d == 0:
        for j in range(pos[1], M):
            if arr[pos[0]][j] == 6:
                break
            arr[pos[0]][j] = do(arr[pos[0]][j])
        for i in range(pos[0], -1, -1):
            if arr[i][pos[1]] == 6:
                break
            arr[i][pos[1]] = do(arr[i][pos[1]])
    elif d == 1:
        for j in range(pos[1], M):
            if arr[pos[0]][j] == 6:
                break
            arr[pos[0]][j] = do(arr[pos[0]][j])
        for i in range(pos[0], N):
            if arr[i][pos[1]] == 6:
                break
            arr[i][pos[1]] = do(arr[i][pos[1]])
    elif d == 2:
        for j in range(pos[1], -1, -1):
            if arr[pos[0]][j] == 6:
                break
            arr[pos[0]][j] = do(arr[pos[0]][j])
        for i in range(pos[0], N):
            if arr[i][pos[1]] == 6:
                break
            arr[i][pos[1]] = do(arr[i][pos[1]])
    else:
        for j in range(pos[1], -1, -1):
            if arr[pos[0]][j] == 6:
                break
            arr[pos[0]][j] = do(arr[pos[0]][j])
        for i in range(pos[0], -1, -1):
            if arr[i][pos[1]] == 6:
                break
            arr[i][pos[1]] = do(arr[i][pos[1]])

    return arr


def cam4(arr, n, d):
    pos = camera[n]
    if d == 0:
        for j in range(pos[1], M):
            if arr[pos[0]][j] == 6:
                break
            arr[pos[0]][j] = do(arr[pos[0]][j])
        for j in range(pos[1], -1, -1):
            if arr[pos[0]][j] == 6:
                break
            arr[pos[0]][j] = do(arr[pos[0]][j])
        for i in range(pos[0], -1, -1):
            if arr[i][pos[1]] == 6:
                break
            arr[i][pos[1]] = do(arr[i][pos[1]])
    elif d == 1:
        for j in range(pos[1], M):
            if arr[pos[0]][j] == 6:
                break
            arr[pos[0]][j] = do(arr[pos[0]][j])
        for i in range(pos[0], N):
            if arr[i][pos[1]] == 6:
                break
            arr[i][pos[1]] = do(arr[i][pos[1]])
        for i in range(pos[0], -1, -1):
            if arr[i][pos[1]] == 6:
                break
            arr[i][pos[1]] = do(arr[i][pos[1]])
    elif d == 2:
        for j in range(pos[1], M):
            if arr[pos[0]][j] == 6:
                break
            arr[pos[0]][j] = do(arr[pos[0]][j])
        for j in range(pos[1], -1, -1):
            if arr[pos[0]][j] == 6:
                break
            arr[pos[0]][j] = do(arr[pos[0]][j])
        for i in range(pos[0], N):
            if arr[i][pos[1]] == 6:
                break
            arr[i][pos[1]] = do(arr[i][pos[1]])
    else:
        for j in range(pos[1], -1, -1):
            if arr[pos[0]][j] == 6:
                break
            arr[pos[0]][j] = do(arr[pos[0]][j])
        for i in range(pos[0], N):
            if arr[i][pos[1]] == 6:
                break
            arr[i][pos[1]] = do(arr[i][pos[1]])
        for i in range(pos[0], -1, -1):
            if arr[i][pos[1]] == 6:
                break
            arr[i][pos[1]] = do(arr[i][pos[1]])

    return arr


def cam5(arr, n):
    pos = camera[n]
    for j in range(pos[1], M):
        if arr[pos[0]][j] == 6:
            break
        arr[pos[0]][j] = do(arr[pos[0]][j])
    for j in range(pos[1], -1, -1):
        if arr[pos[0]][j] == 6:
            break
        arr[pos[0]][j] = do(arr[pos[0]][j])
    for i in range(pos[0], N):
        if arr[i][pos[1]] == 6:
            break
        arr[i][pos[1]] = do(arr[i][pos[1]])
    for i in range(pos[0], -1, -1):
        if arr[i][pos[1]] == 6:
            break
        arr[i][pos[1]] = do(arr[i][pos[1]])

    return arr


def calc(arr):
    sigma = 0

    for i in range(N):
        for j in range(M):
            if not arr[i][j]:
                sigma += 1

    return sigma


def watch(room, n=0):
    global ans

    if ans == 0:
        return

    if n == len(camera):
        result = calc(room)
        if ans > result:
            ans = result

        return

    cctv = room[camera[n][0]][camera[n][1]]
    for d in range(4):
        if ans == 0 or (d > 0 and cctv == 5):
            return
        arr = copy.deepcopy(room)
        if cctv == 1: watch(cam1(arr, n, d), n+1);
        elif cctv == 2: watch(cam2(arr, n, d), n+1);
        elif cctv == 3: watch(cam3(arr, n, d), n+1);
        elif cctv == 4: watch(cam4(arr, n, d), n+1)
        else: watch(cam5(arr, n), n+1)


N, M = map(int, input().strip().split())
test_case = []
camera = []
for i in range(N):
    temp = list(map(int, input().strip().split()))
    for j in range(M):
        if temp[j] in [1, 2, 3, 4, 5]:
            camera.append([i, j])
    test_case.append(temp)

ans = 64

watch(test_case)

print(ans)