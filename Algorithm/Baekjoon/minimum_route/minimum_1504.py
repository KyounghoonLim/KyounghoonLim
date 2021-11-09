from collections import deque

V, E = map(int, input().strip().split())
test_case = [list(map(int, input().strip().split())) for _ in range(E)]
connected = [[] for _ in range(V+1)]
for t in range(E):
    connected[test_case[t][0]].append((test_case[t][1], test_case[t][2]))
    connected[test_case[t][1]].append((test_case[t][0], test_case[t][2]))

must = map(int, input().strip().split())
do = [1, must[0], must[1]]
distance = [[99999999] * (V+1) for _ in range(3)]
for t in range(3):
    queue = deque([do[t]])
    distance[t][do[t]] = 0
    while queue:
        now = queue.popleft()
        for node in connected[now]:
            if distance[t][now] + node[1] < distance[t][node[0]]:
                distance[t][node[0]] = distance[t][now] + node[1]
                queue.append(node[0])

temp, p = 999999999, 0
for t in range(V+1):
    if t != 1 and t != must[0] and t!= must[1]:
        if distance[0][t] + distance[1][t] + distance[2][t] < temp:
            temp = distance[0][t] + distance[1][t] + distance[2][t]
            p = t