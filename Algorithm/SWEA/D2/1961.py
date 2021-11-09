def rotation(arr):
    temp = [[0] * N for _ in range(N)]
    for t_i in range(N):
        for t_j in range(N):
            temp[t_j][N - t_i - 1] = arr[t_i][t_j]

    return temp


T = int(input().strip())

for tc in range(1, T+1):
    N = int(input().strip())
    test_case = [list(map(int, input().strip().split())) for _ in range(N)]
    r_arr_1 = rotation(test_case)
    r_arr_2 = rotation(r_arr_1)
    r_arr_3 = rotation(r_arr_2)
    container = [r_arr_1, r_arr_2, r_arr_3]
    print('#{}' .format(tc))
    for i in range(N):
        for p in range(3):
            for j in range(N):
                if j == N-1:
                    print(container[p][i][j], end=' ')
                else:
                    print(container[p][i][j], end='')
        print()