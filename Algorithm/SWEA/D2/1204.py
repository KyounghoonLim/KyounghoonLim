def my_max():
    maxi = 0
    for t in range(len(temp)):
        if temp[t] >= temp[maxi]:
            maxi = t

    print('#{} {}' .format(case_num, maxi))


T = int(input().strip())

for tc in range(T):
    case_num = int(input().strip())
    test_case = list(map(int, input().strip().split()))

    temp = [0] * 101

    for n in test_case:
        temp[n] += 1

    my_max()
