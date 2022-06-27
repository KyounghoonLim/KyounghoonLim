def solution(n, m, a, b, c, d):
    answer = ''

    test_case = [[] for _ in range(n)]

    for i in range(m):
        test_case[a[i]-1].append(c[i] * 2 + d[i])

    print(test_case)

    return answer

solution(2, 2, [1,1], [2,2], [0,1], [1,0])