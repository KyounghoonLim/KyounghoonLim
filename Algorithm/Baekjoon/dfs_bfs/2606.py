def warm(idx=1, Q=[]):
    global ans

    for t in test_case[idx]:
        if not visited[t]:
            visited[t] = 1
            Q = [t] + Q
            ans += 1
    if Q:
        warm(Q.pop(), Q)

    return


N = int(input().strip())
node = int(input().strip())
temp = [list(map(int, input().strip().split())) for _ in range(node)]
test_case = [[] for _ in range(N+1)]
for net in temp:
    test_case[net[0]].append(net[1])
    test_case[net[1]].append(net[0])
visited = [0] * (N+1)
visited[1] = 1
ans = 0
warm()
print(ans)
