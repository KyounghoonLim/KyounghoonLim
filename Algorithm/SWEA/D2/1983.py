def my_max(arr):
    temp = []
    for t in range(N):
        if not score[t]:
            temp.append(t)
    maxi = temp[0]
    for t in temp:
        if arr[t] > arr[maxi]:
            maxi = t

    return maxi


def exchange(arr):
    s_list = [
        ['A+', N // 10], ['A0', N // 10], ['A-', N // 10], ['B+', N // 10], ['B0', N // 10],
        ['B-', N // 10], ['C+', N // 10], ['C0', N // 10], ['C-', N // 10], ['D0', N // 10],
    ]
    s = 0
    for t in range(N):
        maxi = my_max(arr)
        score[maxi] = s_list[s][0]
        s_list[s][1] -= 1
        if s_list[s][1] == 0:
            s += 1


def total_score():
    t_score = []
    for t in test_case:
        s = round(t[0] * 0.35 + t[1] * 0.45 + t[2] * 0.2, 1)
        t_score.append(s)
    exchange(t_score)


T = int(input().strip())

for tc in range(1, T + 1):
    N, K = map(int, input().strip().split())
    test_case = [list(map(int, input().strip().split())) for _ in range(N)]
    score = [0] * N
    total_score()

    print('#{} {}'.format(tc, score[K-1]))
