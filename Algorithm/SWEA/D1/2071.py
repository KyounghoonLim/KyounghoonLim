def my_avg():
    sigma = 0
    for t in test_case:
        sigma += t
    print('#{} {}' .format(tc, int(round(sigma/len(test_case), 0))))


T = int(input().strip())

for tc in range(1, T+1):
    test_case = list(map(int,input().strip().split()))
    my_avg()