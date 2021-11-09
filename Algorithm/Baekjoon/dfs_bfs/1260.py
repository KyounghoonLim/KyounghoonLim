from collections import deque


def dfs(i):
    result = []

    stack = [i]
    while stack:
        go = stack.pop()
        if not visited[go]:
            visited[go] = True
            result.append(str(go))
        for t in range(len(test_case[go])-1, -1, -1):
            if not visited[test_case[go][t]]:
                stack.append(test_case[go][t])

    print(' '.join(result))

    return


def bfs(i):
    result = []

    visited[i] = True
    Q = deque([i])
    while Q:
        go = Q.popleft()
        result.append(str(go))
        for t in range(len(test_case[go])):
            if not visited[test_case[go][t]]:
                visited[test_case[go][t]] = True
                Q.append(test_case[go][t])

    print(' '.join(result))

    return


N, M, V = map(int, input().strip().split())
temp = [list(map(int, input().strip().split())) for _ in range(M)]
test_case = [[] for _ in range(N+1)]
for i in range(M):
    test_case[temp[i][0]].append(temp[i][1])
    test_case[temp[i][1]].append(temp[i][0])
for i in range(len(test_case)):
    if test_case[i]:
        test_case[i].sort()
for i in range(2):
    visited = [False] * (N+1)
    if i % 2:
        bfs(V)
    else:
        dfs(V)