def rotation(temp, direc):
    if direc == 0:
        temp[1][0], temp[1][1], temp[1][2], temp[3][1] = temp[3][1], temp[1][0], temp[1][1], temp[1][2]
    elif direc == 1:
        temp[1][0], temp[1][1], temp[1][2], temp[3][1] = temp[1][1], temp[1][2], temp[3][1], temp[1][0]
    elif direc == 2:
        temp[0][1], temp[1][1], temp[2][1], temp[3][1] = temp[1][1], temp[2][1], temp[3][1], temp[0][1]
    else:
        temp[0][1], temp[1][1], temp[2][1], temp[3][1] = temp[3][1], temp[0][1], temp[1][1], temp[2][1]

    return temp


di = [0, 0, -1, 1]
dj = [1, -1, 0, 0]

N, M, i, j, K = map(int, input().strip().split())
test_case = [list(map(int, input().strip().split())) for _ in range(N)]
order = list(map(int, input().strip().split()))

dice_flat = [[0, 3, 0], [2, 1, 5], [0, 4, 0], [0, 6, 0]]
dice = [0] * 6
x, y = 1, 1
for n in range(K):
    d = order[n] - 1
    ti = i + di[d]
    tj = j + dj[d]
    if 0 <= ti < N and 0 <= tj < M:
        dice_flat = rotation(dice_flat, d)
        top, bottom = dice_flat[1][1] - 1, dice_flat[3][1] - 1
        if test_case[ti][tj]:
            dice[bottom] = test_case[ti][tj]
            test_case[ti][tj] = 0
        else:
            test_case[ti][tj] = dice[bottom]
        i, j = ti, tj
        print(dice[top])