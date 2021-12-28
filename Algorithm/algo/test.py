import copy


def tst(arr, i=0, times=0, subs=0):
    global ans
    for t in range(i, len(arr)):
        if times + arr[t][1] <= M:
            tst(arr, t+1, times+arr[t][1], subs+arr[t][0])

    if subs > ans:
        ans = subs
    return


T = int(input().strip())
for tc in range(1, T+1):
    N, M = map(int, input().strip().split())

    test_case = [list(map(int, input().strip().split())) for _ in range(N)]
    ans = 0

    for idx in range(N):
        temp = copy.deepcopy(test_case)
        temp[idx][1] //= 2
        tst(temp)

    print('#{} {}' .format(tc, ans))