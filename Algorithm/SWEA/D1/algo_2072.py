def my_sum():
    sigma = 0
    for t in test_case:
        if t % 2:
            sigma += t
    print('#{} {}' .format(tc, sigma))

T = int(input().strip())

for tc in range(1,T+1):
    test_case = list(map(int, input().strip().split()))
    my_sum()