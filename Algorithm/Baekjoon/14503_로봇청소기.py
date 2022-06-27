import pprint

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def can_go(i, j):
    for t in range(4):
        ti, tj = i + di[t], j + dj[t]
        if test_case[ti][tj] == 0 or test_case[ti][tj] == 2:
            return True
    return False


def run(pos, n=1):
    global ans

    for i in range(1-n, n):
        for j in range(1-n, n):
            if 1-n < i < n-1 and 1-n < j < n-1:
                continue

            ni, nj = pos[0] + i, pos[1] + j
            if 0 <= ni < N and 0 <= nj < M and test_case[ni][nj] == 0:
                if can_go(ni, nj):
                    test_case[ni][nj] = 2
                    ans += 1
                else:
                    continue

    if n < max([N, M]):
        run(pos, n+1)
    else:
        return


N, M = map(int,input().split())
pos = list(map(int, input().split()))
test_case = [list(map(int, input().split())) for _ in range(N)]

test_case[pos[0]][pos[1]] = 2
ans = 1

run(pos)

print(ans)
pprint.pprint(test_case)