import copy


def map_helper(tar):
    return int(tar) - 1


def init_ladder():
    ladder = [[0] * N for _ in range(H)]
    for t in range(M):
        x, y = map(map_helper, input().split())
        ladder[x][y], ladder[x][y + 1] = t+1, t+1

    return ladder


def can_make_link(ladder, tar):
    if ladder[tar] != 0 or ladder[tar+1] != 0:  ### 대상 검증 ###
        return False

    return True


def test_ladder(ladder):
    for st in range(N):
        i, j = 0, st
        while i < H:
            if ladder[i][j] == 0:
                pass
            elif j > 0 and ladder[i][j] == ladder[i][j-1]:
                j -= 1
            elif j < N - 1 and ladder[i][j] == ladder[i][j+1]:
                j += 1
            i += 1
        if j != st:
            return False

    return True


def make_ladder(ladder, x=0, y=0, n=0):
    global ans

    if n > 3 or n > ans:
        return

    elif test_ladder(ladder):
        if ans > n:
            ans = n
        return

    else:
        for i in range(x, H):
            if i != x:
                y = 0
            for j in range(y, N-1):
                if not can_make_link(ladder[i], j):
                    continue
                ladder[i][j], ladder[i][j+1] = M+n+1, M+n+1 ### 가로연결선 번호 매김 ###
                make_ladder(ladder, i, j, n+1)
                ladder[i][j], ladder[i][j+1] = 0, 0


N, M, H = map(int, input().split())
test_case = init_ladder()
ans = 987654321

make_ladder(copy.deepcopy(test_case))

print(ans if 0 <= ans <= 3 else '-1')