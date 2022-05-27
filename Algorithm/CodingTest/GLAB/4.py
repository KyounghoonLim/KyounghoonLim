import copy


def triangle_direction(i, j):
    if not i % 2:
        if not j % 2:
            return True
        return False
    else:
        if not j % 2:
            return False
        return True


def triangle_chess(arr, st_i, st_j, n, N, rooks):
    global answer

    if not rooks:
        answer += 1

        return

    for i in range(st_i, n):
        t = n - i - 1
        if i != st_i:
            st_j = t
        for j in range(st_j, N - t):
            if arr[i][j] == 1:
                if rooks == 1:
                    triangle_chess(arr, st_i, st_j, n, N, 0)
                    continue
                _arr = copy.deepcopy(arr)
                _arr[i][j] = 'R'
                for k in range(1, N):
                    # 좌측
                    if 0 <= j-k < N and _arr[i][j-k] == 1:
                        _arr[i][j-k] = -1
                    # 우측
                    if 0 <= j+k < N and _arr[i][j+k] == 1:
                        _arr[i][j+k] = -1
                    # 좌측 위
                    if 0 <= i-k < n and 0 <= j-k < N and _arr[i-k][j-k] == 1:
                        _arr[i-k][j-k] = -1
                        if triangle_direction(i, j):
                            t = -1
                        else:
                            t = 1
                        if 0 <= i-k < N and 0 <= j-k+t < N and _arr[i-k][j-k+t] == 1:
                            _arr[i-k][j-k+t] = -1
                    # 우측 아래
                    if 0 <= i+k < n and 0 <= j+k < N and _arr[i+k][j+k] == 1:
                        _arr[i+k][j+k] = -1
                        if triangle_direction(i, j):
                            t = -1
                        else:
                            t = 1
                        if 0 <= i+k < N and 0 <= j+k+t < N and _arr[i+k][j+k+t] == 1:
                            _arr[i+k][j+k+t] = -1
                    # 우측 위
                    if 0 <= i-k < n and 0 <= j+k < N and _arr[i-k][j+k] == 1:
                        _arr[i-k][j+k] = -1
                        if triangle_direction(i, j):
                            t = 1
                        else:
                            t = -1
                        if 0 <= i-k < N and 0 <= j+k+t < N and _arr[i-k][j+k+t] == 1:
                            _arr[i-k][j+k+t] = -1
                    # 좌측 아래
                    if 0 <= i+k < n and 0 <= j-k < N and _arr[i+k][j-k] == 1:
                        _arr[i+k][j-k] = -1
                        if triangle_direction(i, j):
                            t = 1
                        else:
                            t = -1
                        if 0 <= i+k < N and 0 <= j-k+t < N and _arr[i+k][j-k+t] == 1:
                            _arr[i+k][j-k+t] = -1

                triangle_chess(_arr, i, j, n , N, rooks-1)


def solution(n, rooks):
    global answer
    N = n * 2 - 1
    test_case = [[1] * N for _ in range(n)]
    for i in range(n):
        for t in range(n - i - 1):
            test_case[i][t], test_case[i][N - t - 1] = 0, 0

    triangle_chess(copy.deepcopy(test_case), 0, N // 2, n, N, rooks)

    return answer


answer = 0
print(solution(5,3))