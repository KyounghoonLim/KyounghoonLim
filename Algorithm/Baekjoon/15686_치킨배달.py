def find_target(arr, n, target):
    temp = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] == target:
                temp.append([i, j])

    return temp


def find_min_distance(start, comb):
    result = 0
    temp = [[] for _ in range(len(start))]

    for ele in comb:
        for i in range(len(start)):
            target = start[i]
            temp[i].append(abs(ele[0] - target[0]) + abs(ele[1] - target[1]))

    for t in range(len(temp)):
        result += min(temp[t])

    return result


def sum_of_min_distance(start, destination, comb, target, st=0, n=0):
    global ans

    if len(comb) == target:
        result = find_min_distance(start, comb)
        if ans > result:
            ans = result
        return
    else:
        for i in range(st, len(destination)):
            comb.append(destination[i])
            sum_of_min_distance(start, destination, comb, target, i+1, n+1)
            comb.pop()


N, M = map(int, input().split())
test_case = [list(map(int, input().split())) for _ in range(N)]
houses = find_target(test_case, N, 1)
restaurant = find_target(test_case, N, 2)

ans = 987654321

sum_of_min_distance(houses, restaurant, [], M)
print(ans)


