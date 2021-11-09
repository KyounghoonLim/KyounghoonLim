# di = [-1, -1, 0, 1, 1, 1, 0, -1]
# dj = [0, 1, 1, 1, 0, -1, -1, -1]
# T = int(input().strip())
#
# for tc in range(1, T + 1):
#     N = int(input().strip())
#     test_case = [input().strip() for _ in range(N)]
#
#     Q = []
#     visited

def find_start(i, j):
    if i >= N - 1 and j >= N - 1:
        return
    if j >= N - 1:
        i += 1
        j = 0
    for t_i in range(i, N):
        for t_j in range(j, N):
            if test_case[t_i][t_j] == 'o':
                return t_i, t_j


def is_go(i=0, j=0, d=-1, cnt=0):
    if d >= 0:
        cnt += 1
        if cnt == 5:
            return True
        ti = i + di[d]
        tj = j + dj[d]
        if 0 <= ti < N and 0 <= tj < N:
            if test_case[ti][tj] == 'o':
                if is_go(ti, tj, d, cnt):
                    return True
    else:
        i, j = find_start(i, j)
        direc = []
        for t in range(8):
            ti = i + di[t]
            tj = j + dj[t]
            if 0 <= ti < N and 0 <= tj < N:
                if test_case[ti][tj] == 'o':
                    direc.append(t)
        if direc:
            for t1 in range(len(direc)):
                d = direc.pop(0)
                if is_go(i + di[d], j + dj[d], d, 1):
                    return True
        while i < N - 1 and j < N - 1:
            j += 1
            if is_go(i, j):
                return True


di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, 1, 1, 1, 0, -1, -1, -1]
T = int(input().strip())

for tc in range(1, T + 1):
    N = int(input().strip())
    test_case = [input().strip() for _ in range(N)]
    if is_go():
        print('#{} YES'.format(tc))
    else:
        print('#{} NO'.format(tc))
