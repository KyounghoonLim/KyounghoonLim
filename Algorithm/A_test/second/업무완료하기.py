import copy


def is_complete(arr=[]):
    if arr:
        for t in arr[1:]:
            if not visited[t]:
                return False
    else:
        for t in range(1, N+1):
            if not visited[t]:
                return False

    return True


def work(arr, n=0):
    if n == 5000:
        return False
    if is_complete():
        return True
    for t1 in range(N):
        if not visited[t1+1]:
            if is_complete(arr[t1]):
                temp = []
                for t2 in arr[t1][1:]:
                    if t2 == 0 or visited[t2]:
                        temp.append(visited[t2])
                visited[t1+1] = max(temp) + arr[t1][0]
    return work(arr, n+1)


T = int(input().strip())

for tc in range(1, T+1):
    N = int(input().strip())
    test_case = [list(map(int, input().strip().split())) for _ in range(N)]

    ans, p, flag = 99999999999, 0, 0
    while p < N:
        visited = [0] * (N+1)
        visited[0] = 1
        sample = copy.deepcopy(test_case)
        sample[p][0] //= 2
        if not work(sample):
            print('#{} -1' .format(tc))
            flag = 1
            break
        else:
            total_times = max(visited)
            if ans > total_times - 1:
                ans = total_times - 1
            p += 1
    if not flag:
        print('#{} {}' . format(tc, ans))
