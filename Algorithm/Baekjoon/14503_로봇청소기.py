import pprint


di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def go_next(pos:list, t):
    next_pos = pos.copy()
    next_pos[2] = (pos[2] + t) % 4
    next_pos[1] += dj[next_pos[2]]
    next_pos[0] += di[next_pos[2]]
    if can_go(next_pos):
        return next_pos
    else:
        return False


def go_back(pos:list):
    d = (pos[2] + 2) % 4
    back_pos = pos.copy()
    back_pos[0] += di[d]
    back_pos[1] += dj[d]
    if can_back(back_pos):
        return back_pos
    else:
        return False


def can_go(pos):
    ti, tj = pos[0], pos[1]
    if 0 <= ti < N and 0 <= tj < M and test_case[ti][tj] == 0:
        return True
    return False


def can_back(pos):
    ti, tj = pos[0], pos[1]
    if 0 <= ti < N and 0 <= tj < M and test_case[ti][tj] != 1:
        return True
    return False


def run(pos, n=-1):
    global ans, FLAG

    i, j = pos[0], pos[1]
    flag = False
    if test_case[i][j] == 0:
        test_case[i][j] = n
        ans += 1

    for t in range(1, 5):
        next_pos = go_next(pos, -t)
        if next_pos:
            flag = True
            run(next_pos, n-1)
            if FLAG:
                return
    else:
        if not flag:
            back_pos = go_back(pos)
            if back_pos:
                run(back_pos, n)
            else:
                FLAG = True
                return


N, M = map(int,input().split())
pos = list(map(int, input().split()))
test_case = [list(map(int, input().split())) for _ in range(N)]

ans = 0
FLAG = False

run(pos)

print(ans)
pprint.pprint(test_case)