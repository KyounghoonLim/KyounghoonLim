import heapq

V, E = map(int, input().strip().split())
K = int(input().strip())
test_case = [list(map(int, input().strip().split())) for _ in range(E)]
connected = [[] for _ in range(V+1)]
for t in range(E):
    connected[test_case[t][0]].append((test_case[t][1], test_case[t][2]))

distance = [99999999999] * (V+1)
distance[K] = 0

heap = []
heapq.heappush(heap, (0, 1))
while heap:
    weight, now = heapq.heappop(heap)
    for node in connected[now]:
        if distance[now] + node[1] < distance[node[0]]:
            distance[node[0]] = distance[now] + node[1]
            heapq.heappush(heap, (node[1], node[0]))

for t in range(1, V+1):
    if distance[t] == 99999999999:
        print('INF')
        continue
    print(distance[t])