def my_avg():
    sigma = 0
    cnt = 0
    for t in range(1, len(test_case)):
        sigma += test_case[t]
    avg = sigma // test_case[0]
    for t in range(1, len(test_case)):
        if test_case[t] > avg:
            cnt += 1

    return cnt / test_case[0] * 100


N = int(input().strip())

for tc in range(N):
    test_case = list(map(int, input().strip().split()))

    print('{:.3f}%' .format(my_avg()))