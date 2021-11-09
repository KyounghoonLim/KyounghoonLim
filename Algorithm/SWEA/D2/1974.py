def is_sudoku():
    for t_i in range(9):
        temp_i = set()
        temp_j = set()
        for t_j in range(9):
            temp_i.add(test_case[t_i][t_j])
            temp_j.add(test_case[t_j][t_i])
        if len(temp_i) != 9 or len(temp_j) != 9:
            return
    t = 0
    while t < 9:
        temp_st = set()
        temp_nd = set()
        temp_rd = set()
        for t_i in range(t, t+3):
            for t_j in range(3):
                temp_st.add(test_case[t_i][t_j])
                temp_nd.add(test_case[t_i][t_j+3])
                temp_rd.add(test_case[t_i][t_j+6])
        if len(temp_st) != 9 or len(temp_nd) != 9 or len(temp_rd) != 9:
            return
        t += 3
    return True


T = int(input().strip())

for tc in range(1, T+1):
    test_case = [list(map(int, input().strip().split())) for _ in range(9)]

    if is_sudoku():
        print('#{} 1' .format(tc))
    else:
        print('#{} 0' .format(tc))