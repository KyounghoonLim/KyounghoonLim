N = int(input().strip())

for tc in range(N):
    test_case = input().strip()
    i, j, cnt = 0, 1, 0
    while i < len(test_case):
        if test_case[i] == 'O':
            cnt += j
            j += 1
        else:
            j = 1
        i += 1

    print(cnt)