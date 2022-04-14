T = int(input().strip())

for tc in range(1, T+1):
    N, K = map(int, input().strip().split())
    test_case = list(map(int, input().strip().split()))
    need_time = list(map(int, input().strip().split()))

    visited = [[] * K for _ in range(K)]
    for t in range(N):
        visited[test_case[t]-1].append(t)

    for t2 in range(K):
        for t3 in range(len(visited[t2])):
            visited[t2][t3] = need_time[visited[t2][t3]]
        visited[t2].sort()

    temp = []
    for t4 in range(K):
        if len(visited[t4]) > 1:
            temp.extend(visited[t4][:-1])

    temp.sort()
    ans = 0
    for t5 in range(K-len(set(test_case))):
        ans += temp[t5]

    print('#{} {}' .format(tc, ans))