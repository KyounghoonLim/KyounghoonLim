T = int(input().strip())

for tc in range(1, T + 1):
    N = int(input().strip())
    test_case = [input().split() for _ in range(N)]
    for temp in test_case:
        temp[1] = int(temp[1])

    print('#{}' .format(tc))
    p = 0
    while p < N:
        for t in range(10):
            print(test_case[p][0], end='')
            test_case[p][1] -= 1
            if test_case[N-1][1] == 0:
                p += 1
                break
            if test_case[p][1] == 0:
                p += 1
        print()