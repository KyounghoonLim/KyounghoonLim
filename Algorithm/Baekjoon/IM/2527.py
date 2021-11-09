def is_merge():
    flag = 0
    for t_i in range(square[0][1], square[0][3]):
        for t_j in range(square[0][2], square[0][3]):
            if temp[t_i][t_j] == 3:
                return 'a'
            if 0 <= t_i + 1 < len(temp) and 0 <= t_j + 1 < len(temp):
                if temp[t_i+1][t_j] == 1 or temp[t_i][t_j+1] == 2:
                    return 'b'
            if 0 <= t_i + 1 < len(temp) and 0 <= t_j + 1 < len(temp):
                if temp[t_i+1][t_j+1] == 2:
                    flag = 1
            if 0 <= t_i - 1 < len(temp) and 0 <= t_j + 1 < len(temp):
                if temp[t_i-1][t_j+1] == 2:
                    flag = 1
    if flag:
        return 'c'
    else:
        return 'd'


for tc in range(4):
    test_case = list(map(int, input().strip().split()))
    temp = [[0] * max(test_case) for _ in range(max(test_case))]
    square = [test_case[:4], test_case[4:]]
    k = 0
    for sq in square:
        k += 1
        for i in range(sq[1], sq[3]):
            for j in range(sq[0], sq[2]):
                temp[i][j] += k
    print(is_merge())