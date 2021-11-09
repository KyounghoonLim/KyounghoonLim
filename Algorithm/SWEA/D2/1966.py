def my_sort():
    for t1 in range(N-1):
        mini = t1
        for t2 in range(t1+1, N):
            if test_case[mini] > test_case[t2]:
                mini = t2
        test_case[t1], test_case[mini] = test_case[mini], test_case[t1]


T = int(input().strip())

for tc in range(1, T+1):
    N = int(input().strip())
    test_case = list(map(int, input().strip().split()))
    my_sort()
    print('#{}' .format(tc), end=' ')
    for n in test_case:
        print('{}' .format(n), end=' ')
    print()