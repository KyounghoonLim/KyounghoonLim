T = int(input().strip())

for tc in range(1, T+1):
    test_case = list(map(int, input().strip().split()))
    h = test_case[0] + test_case[2]
    m = test_case[1] + test_case[3]
    if m > 60:
        m -= 60
        h += 1
    if h > 12:
        h -= 12
        
    print('#{} {} {}' .format(tc, h, m))