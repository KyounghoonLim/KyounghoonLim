def my_sort(arr):
    for t in range(len(arr)-1):
        mini = t
        for t2 in range(t+1, len(arr)):
            if ord(arr[t2]) < ord(arr[mini]):
                mini = t2
        arr[t], arr[mini] = arr[mini], arr[t]

    return arr


T = int(input().strip())

for tc in range(1, T+1):
    N = int(input().strip())
    test_case = [input().strip() for _ in range(N)]
    temp = set()
    for title in test_case:
        temp.add(title[0])

    ans = my_sort(list(temp))
    cnt = 0
    for i in range(len(ans)):
        if ord(ans[i]) + cnt != 65 + cnt:
            break
        cnt += 1

    print('#{} {}' .format(tc, cnt))