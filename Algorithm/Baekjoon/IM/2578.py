def choose(n):
    for t_i in range(5):
        for t_j in range(5):
            if test_case[t_i][t_j] == n:
                test_case[t_i][t_j] = 'x'
                return


def is_bingo_i():
    for t_i in range(5):
        cnt_i = 0
        for t_j in range(5):
            if bingo_i[t_i] == 0 and test_case[t_i][t_j] == 'x':
                cnt_i += 1
        if cnt_i == 5:
            bingo_i[t_i] = 1
            return True


def is_bingo_j():
    for t_j in range(5):
        cnt_j = 0
        for t_i in range(5):
            if bingo_j[t_j] == 0 and test_case[t_i][t_j] == 'x':
                cnt_j += 1
        if cnt_j == 5:
            bingo_j[t_j] = 1
            return True


def is_bingo_c():
    cnt_lc, cnt_rc = 0, 0
    for t_i in range(5):
        if bingo_c[0] == 0 and test_case[t_i][t_i] == 'x':
            cnt_lc += 1
        if bingo_c[1] == 1 and test_case[t_i][5 - t_i - 1] == 'x':
            cnt_rc += 1
    if cnt_lc == 5:
        bingo_c[0] = 1
        return True
    if cnt_rc == 5:
        bingo_c[1] = 1
        return True

test_case = [list(map(int, input().strip().split())) for _ in range(5)]
announce = [list(map(int, input().strip().split())) for _ in range(5)]
cnt, flag = 0, 0
bingo_i = [0] * 5
bingo_j = [0] * 5
bingo_c = [0, 0]
for i in range(5):
    for j in range(5):
        choose(announce[i][j])
        cnt += 1
        if is_bingo_i():
            flag += 1
        if is_bingo_j():
            flag += 1
        if is_bingo_c():
            flag += 1
        if flag == 3:
            break
    if flag == 3:
        break
print(cnt)
