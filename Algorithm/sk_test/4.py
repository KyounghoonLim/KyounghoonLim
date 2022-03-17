def solution(n, edges):
    answer = 0

    arr = [[] for _ in range(n)]
    for edge in edges:
        arr[edge[0]].append(edge[1])
        arr[edge[1]].append(edge[0])
    temp = [[0] * n for _ in range(n)]
    for i in range(n):
        stack = []
        temp[i][i] = -1
        for j in arr[i]:
            stack.append((j, 1))
        while stack:
            node = stack.pop()
            if not temp[i][node[0]] or temp[i][node[0]] > node[1]:
                temp[i][node[0]] = node[1]
            for k in arr[node[0]]:
                if not temp[i][k] or temp[i][k] > node[1] + 1:
                    stack.append((k, node[1] + 1))

    for _i in range(n):
        for _j in range(n):
            if _i == _j:
                continue
            for _k in range(n):
                if _i == _k or _j == _k:
                    continue
                if temp[_i][_j] + temp[_j][_k] == temp[_i][_k]:
                    answer += 1

    return answer


print(solution(5, [[0,1],[0,2],[1,3],[1,4]]	))