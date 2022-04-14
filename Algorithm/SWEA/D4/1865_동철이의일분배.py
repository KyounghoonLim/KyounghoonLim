def max_efficiency(employee=0, efficiency=1):
    global ans

    if employee == N:
        if efficiency > ans:
            ans = efficiency
        return

    for idx in range(N):
        if not task[idx] and (efficiency * test_case[employee][idx] > ans):
            task[idx] = True
            max_efficiency(employee+1, efficiency * test_case[employee][idx])
            task[idx] = False


def map_input(temp):
    result = int(temp) / 100
    return result


T = int(input().strip())

for tc in range(1, T+1):
    N = int(input().strip())
    test_case = [list(map(map_input, input().strip().split())) for _ in range(N)]
    task = [False] * N
    ans = 0
    max_efficiency()

    print('#{} {:.6f}' .format(tc, ans * 100))