def solution(n, m, x, y, z):
    answer = []

    test_case = []
    rank = [[_, 0] for _ in range(n+1)]
    mini = min(z)

    for i in range(m):
        test_case.append([x[i], y[i], z[i], i+1])
        if z[i] == mini:
            rank[x[i]][1] -= 1
            rank[y[i]][1] -= 1

    for j in range(m):
        node_rank = rank[test_case[j][0]][1] + rank[test_case[j][1]][1]
        test_case[j].append(node_rank)

    test_case.sort(key=lambda x:(x[4], x[2], x[3], x[0], x[1]))

    print(test_case)
    for k in range(m):
        answer.append(test_case[k][3])

    return answer


print(solution(3, 3, [1, 1, 2], [3, 2, 3], [1, 5, 2]))
print(solution(4, 4, [1, 1, 3, 4], [3, 4, 2, 2], [2, 1, 1, 2]))