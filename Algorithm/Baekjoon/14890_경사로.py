import pprint


def is_continuous(target_load, temp=None):
    if temp:
        for t in range(N-1):
            if target_load[t] != target_load[t+1]:
                if temp[t] < L:
                    return False
    else:
        target = target_load.index(min(target_load))
        if target > len(target_load) - L:
            return False
        for t in range(L):
            if target_load[target + t] != target_load[target]:
                return False

    return True


def can_make_load_h(i):
    temp = [1] * N
    for j in range(N-L):
        for k in range(1, L+1):
            if test_case[i][j + k - 1] == test_case[i][j + k] and temp[j + k] == 1:
                temp[j + k] = temp[j + k - 1] + 1
            if abs(test_case[i][j] - test_case[i][j + k]) > 1:  # 높이 체크
                return False
            elif visited[i][j + k]: # 경사로 존재 여부 체크
                return False
    target_load = [test_case[i][t] for t in range(N)]
    for t in range(N-1, 0, -1):
        for u in range(t, -1, -1):
            if target_load[t] == target_load[u]:
                temp[u] = temp[t]
            else:
                break
    if not is_continuous(target_load, temp):  # 연속성 체크
        return False

    return True


def can_make_load_v(i):
    temp = [1] * N
    for j in range(N-L):
        for k in range(1, L+1):
            if test_case[j + k - 1][i] == test_case[j + k][i] and temp[j + k] == 1:
                temp[j + k] = temp[j + k - 1] + 1
            if abs(test_case[j][i] - test_case[j + k][i]) > 1:  # 높이 체크
                return False
            elif visited[j + k][i]: # 경사로 존재 여부 체크
                return False
    target_load = [test_case[t][i] for t in range(N)]
    for t in range(N - 1, 0, -1):
        for u in range(t, -1, -1):
            if target_load[t] == target_load[u]:
                temp[u] = temp[t]
    if not is_continuous(target_load, temp):  # 연속성 체크
        return False

    return True


def make_load_h():
    global ans

    for i in range(N):
        if not can_make_load_h(i):
            continue
        print('h', i)
        for j in range(N - L):
            temp_load = [test_case[i][j + t] for t in range(L+1)]
            if test_case[i][j] == test_case[i][j+L] or not is_continuous(temp_load):
                continue
            for k in range(L):
                visited[i][j+k] = 1
        ans += 1


def make_load_v():
    global ans

    for i in range(N):
        if not can_make_load_v(i):
            continue
        print('v', i)
        for j in range(N - L):
            temp_load = [test_case[j + t][i] for t in range(L + 1)]
            if test_case[j][i] == test_case[j + L][i] or not is_continuous(temp_load):
                continue
            for k in range(L):
                visited[j + k][i] = 1
        ans += 1


N, L = map(int, input().split())
test_case = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

ans = 0

make_load_h()
make_load_v()

print(ans)
pprint.pprint(visited)