def find_target(arr, n, target):
    temp = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] == target:
                temp.append([i, j])

    return temp


def sum_of_min_distance(start, destination, comb, target, st=0, n=0, ans=987654321):
    if len(comb) == target:

    else:
        for i in range(st, len(destination)):
            comb.append(destination[i])
            


N, M = map(int, input().split())
test_case = [list(map(int, input().split())) for _ in range(N)]
houses = find_target(test_case, N, 1)
restaurant = find_target(test_case, N, 2)


