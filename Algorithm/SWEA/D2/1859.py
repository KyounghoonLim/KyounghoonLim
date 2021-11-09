def my_max(idx):
    maxi = idx
    for t in range(idx, N):
        if test_case[t] > test_case[maxi]:
            maxi = t
    return maxi


T = int(input().strip())

for tc in range(1,T+1):
    N = int(input().strip())
    test_case = list(map(int, input().strip().split()))

    benefit = 0
    maxi = 0
    for i in range(N):
        if i > maxi:
            maxi = test_case[my_max(i)]
        if test_case[i] < maxi:
            benefit += maxi - test_case[i]

    print('#{} {}' .format(tc, benefit))