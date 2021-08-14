T = int(input().strip())
result = []

for tc in range(T):
    test_case = []
    N, K = map(int, input().strip().split())
    for input_list in range(N):
        test_case.append(list(map(int, input().strip().split())))

    possible_row = []
    possible_col = []
    for i in range(N):
        for j in range(N):
            space_row = 0
            space_col = 0
            for k in range(N-j):
                if test_case[i][j]:
                    if j == N-1 and test_case[i][j]:
                        space_col += 1
                    elif 0 < j < N and test_case[i][j-1] == 0:
                        if test_case[i][j+k]:
                            space_col += 1
                if test_case[j][i]:
                    if j == N-1 and test_case[j][i]:
                        space_row += 1
                    elif 0 < j < N and test_case[j-1][i] == 0:
                        if test_case[j+k][i]:
                            space_row += 1
            possible_row.append(space_row)
            possible_col.append(space_col)
    print(possible_row, possible_col)
    possibility = 0
    for can_words_in_row in possible_row:
        if K == can_words_in_row:
            possibility += 1
    for can_words_in_col in possible_col:
        if K == can_words_in_col:
            possibility += 1

    result.append(possibility)

for i in range(len(result)):
    print('#{} {}' .format(i+1, result[i]))
