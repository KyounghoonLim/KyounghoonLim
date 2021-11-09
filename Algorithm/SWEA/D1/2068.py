def my_max():
    maxi = test_case[0]
    for t in range(1,len(test_case)):
        if test_case[t] > maxi:
            maxi = test_case[t]
    print('#{} {}' .format(tc, maxi))


T = int(input().strip())

for tc in range(1,T+1):
    test_case = list(map(int,input().strip().split()))
    my_max()