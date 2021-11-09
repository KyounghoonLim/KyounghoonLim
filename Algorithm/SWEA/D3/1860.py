def my_sort():
    for t in range(len(test_case) - 1):
        mini = t
        for t2 in range(t + 1, len(test_case)):
            if test_case[mini] > test_case[t2]:
                mini = t2
        test_case[t], test_case[mini] = test_case[mini], test_case[t]


def bake():
    cnt = [0, 0]
    for i in test_case:
        if cnt[1]:
            cnt[1] -= 1
            continue
        cnt[0] += M
        cnt[1] += K
        if i >= cnt[0] and cnt[1]:
            cnt[1] -= 1
        else:
            print('#{} Impossible'.format(tc))
            return
    print('#{} Possible'.format(tc))


T = int(input().strip())

for tc in range(1, T + 1):
    N, M, K = map(int, input().strip().split())
    test_case = list(map(int, input().strip().split()))
    my_sort()
    bake()
