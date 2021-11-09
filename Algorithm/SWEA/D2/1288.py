T = int(input().strip())

for tc in range(1, T+1):
    test_case = int(input().strip())
    temp = test_case
    num_set = set()
    cnt = 0
    while True:
        for i in str(temp):
            num_set.add(i)
        if len(num_set) == 10:
            break
        cnt += 1
        temp += test_case

    print('#{} {}' .format(tc, temp))