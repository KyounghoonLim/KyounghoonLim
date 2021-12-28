def spend_times(go, in_stair, this_times=0):
    global ans

    if this_times > ans:
        return
    if (not go[0] and not go[1]) and (not in_stair[0] and not in_stair[1]):
        if this_times - 1 < ans:
            ans = this_times - 1
        return
    for t_i in range(2):
        in_stair[t_i].sort(reverse=True)
        for t_k in range(len(in_stair[t_i]) - 1, -1, -1):
            if in_stair[t_i][t_k] < this_times:
                in_stair[t_i].pop()
        for t_j in range(len(go[t_i])-1, -1, -1):
            if go[t_i][t_j] <= this_times and len(in_stair[t_i]) < 3:
                go[t_i].pop()
                in_stair[t_i].append(this_times + stairs[t_i][2])

    spend_times(go, in_stair, this_times+1)


def go_to_lunch(go, n=0):
    if n >= len(times):
        spend_times([sorted(go[0], reverse=True), sorted(go[1], reverse=True)], [[], []])
        return
    for t_i in range(2):
        go[t_i].append(times[n][t_i])
        go_to_lunch(go, n+1)
        go[t_i].pop()


T = int(input().strip())

for tc in range(1, T+1):
    N = int(input().strip())
    test_case = [list(map(int, input().strip().split())) for _ in range(N)]
    people = []
    stairs = []

    for i in range(N):
        for j in range(N):
            if test_case[i][j] > 1:
                stairs.append([i, j, test_case[i][j]])
            elif test_case[i][j] == 1:
                people.append([i, j])

    times = []
    for person in people:
        need_to_times = []
        for stair in stairs:
            need_to_times.append(
                (abs(person[0] - stair[0]) + abs(person[1] - stair[1]))
            )
        times.append(need_to_times)
    ans = 99999999
    go_to_lunch([[], []])

    print('#{} {}' .format(tc, ans))