def find_fish(depth):
    fish = [0] * C
    for i in range(depth):
        for j in range(C):
            if not fish[j]:
                fish[j] = test_case[i][j]
    for feed in fish:
        if 0 < feed < 2:
            return True
    return False


def feeding(now=0, depth=1, times=1):
    global ans

    if depth > R:
        depth = R
    if find_fish(depth):
        for i in range(depth):
            for j in range(C):
                if test_case[i][j] == 1:
                    test_case[i][j] = 0
                    feeding(j, depth+1, times+abs(now-j)+1)
                    test_case[i][j] = 1
    else:
        if ans > times:
            ans = times
        return


T = int(input().strip())

for tc in range(1, T+1):
    R, C = map(int, input().strip().split())
    test_case = [list(map(int, input().strip().split())) for _ in range(R)]

    ans = 9999999
    feeding()

    print('#{} {}' .format(tc, ans))