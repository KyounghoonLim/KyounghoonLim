def my_max(arr):
    maxi = 0
    if complete[0]:
        maxi = 1
        if complete[1]:
            return 2
    for t in range(3):
        if arr[t] > arr[maxi]:
            maxi = t

    return maxi


def drawing(arr):
    global cnt
    tar = my_max(arr)
    if complete[0]:
        if tar == 0:
            return
        else:
            if complete[1]:
                if tar == 1:
                    return
    cnt += M - arr[tar]
    if tar == 1:
        if not complete[0]:
            complete[0] = True
    elif tar == 2:
        if not complete[1]:
            complete[1] = True


T = int(input().strip())

for tc in range(1, T + 1):
    N, M = map(int, input().strip().split())
    test_case = [input().strip() for _ in range(N)]
    cnt = 0
    complete = [False, False]
    Q = []
    for i in range(N):
        temp = [0, 0, 0]
        for j in range(M):
            if i == 0:
                if test_case[i][j] == 'W':
                    temp[0] += 1
            elif i == N-1:
                if test_case[i][j] == 'R':
                    temp[2] += 1
            elif not complete[0] and test_case[i][j] == 'W':
                temp[0] += 1
            elif not complete[1] and test_case[i][j] == 'B':
                temp[1] += 1
            elif test_case[i][j] == 'R':
                temp[2] += 1
        drawing(temp)

    print('#{} {}' .format(tc, cnt))