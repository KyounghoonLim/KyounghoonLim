T = int(input().strip())

for tc in range(1, T+1):
    test_case = int(input().strip())
    cash = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    ans = [0] * 8
    i = 0
    while i < 8:
        if test_case >= cash[i]:
            test_case -= cash[i]
            ans[i] += 1
        else:
            i += 1

    print('#{}' .format(tc))
    for t in ans:
        print('{}' .format(t), end=' ')
    print()