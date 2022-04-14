T = int(input().strip())

for tc in range(1, T+1):
    if tc != T:
        test_case = [list(input().strip()) for _ in range(5)]
    else:
        test_case = [list(input().strip()) for _ in range(4)]
    is_over = True
    ans = ''
    for i in range(4):
        sets = {
            'row': {'O': 0, 'X': 0, 'T': 0, '.': 0},
            'col': {'O': 0, 'X': 0, 'T': 0, '.': 0},
            'crs': {'O': 0, 'X': 0, 'T': 0, '.': 0},
            'r_crs': {'O': 0, 'X': 0, 'T': 0, '.': 0}
        }

        for j in range(4):
            if i == 0:
                sets['crs'][test_case[j][j]] += 1
                sets['r_crs'][test_case[j][3-j]] += 1
            sets['row'][test_case[i][j]] += 1
            sets['col'][test_case[j][i]] += 1
        for key in sets:
            if sets[key]['T']:
                sets[key]['O'] += 1
                sets[key]['X'] += 1
            if sets[key]['.']:
                is_over = False
            if sets[key]['O'] == 4:
                ans = 'O'
            elif sets[key]['X'] == 4:
                ans = 'X'

    if ans:
        print('#{} {} won' .format(tc, ans))
    else:
        if not is_over:
            print('#{} Game has not completed' .format(tc))
        else:
            print('#{} Draw' .format(tc))