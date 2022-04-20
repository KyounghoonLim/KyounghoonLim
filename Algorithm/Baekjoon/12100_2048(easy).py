import copy

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def sort_arr(arr, d):
    for i in range(N):
        for j in range(N):
            if d == 0 and not arr[j][i]:
                for k in range(j + 1, N):
                    if arr[k][i]:
                        arr[j][i], arr[k][i] = arr[k][i], 0
                        break
            elif d == 1 and not arr[i][N - j-1]:
                for k in range(j + 1, N):
                    if arr[i][N - k - 1]:
                        arr[i][N - j - 1], arr[i][N - k - 1] = arr[i][N - k - 1], 0
                        break
            elif d == 2 and not arr[N - j-1][i]:
                for k in range(j + 1, N):
                    if arr[N - k - 1][i]:
                        arr[N - j-1][i], arr[N - k - 1][i] = arr[N - k - 1][i], 0
                        break
            elif d == 3 and not arr[i][j]:
                for k in range(j + 1, N):
                    if arr[i][k]:
                        arr[i][j], arr[i][k] = arr[i][k], 0
                        break

    return arr


def find_max(arr):
    maxi = 0
    for i in range(N):
        if max(arr[i]) > maxi:
            maxi = max(arr[i])

    return maxi

def game(arr, n=0):
    global ans

    if n == 5:
        M = find_max(arr)
        if M > ans:
            ans = M

        return

    for t in range(4):
        temp = copy.deepcopy(arr)
        for i in range(N):
            for j in range(N):
                if t == 0 and temp[j][i]:
                    for k in range(j+1, N):
                        if temp[k][i]:
                            if temp[j][i] == temp[k][i]:
                                temp[j][i], temp[k][i] = temp[j][i] * 2, 0
                            break
                elif t == 1 and temp[i][N-j-1]:
                    for k in range(j+1, N):
                        if temp[i][N-k-1]:
                            if temp[i][N-j-1] == temp[i][N-k-1]:
                                temp[i][N-j-1], temp[i][N-k-1] = temp[i][N-j-1] * 2, 0
                            break
                elif t == 2 and temp[N-j-1][i]:
                    for k in range(j+1, N):
                        if temp[N-k-1][i]:
                            if temp[N-j-1][i] == temp[N-k-1][i]:
                                temp[N-j-1][i], temp[N-k-1][i] = temp[N-j-1][i] * 2, 0
                            break
                elif t == 3 and temp[i][j]:
                    for k in range(j+1, N):
                        if temp[i][k]:
                            if temp[i][j] == temp[i][k]:
                                temp[i][j], temp[i][k] = temp[i][j] * 2, 0
                            break
        game(sort_arr(temp, t), n+1)


N = int(input())
test_case = [list(map(int, input().split())) for _ in range(N)]

ans = 0

game(copy.deepcopy(test_case))

print(ans)