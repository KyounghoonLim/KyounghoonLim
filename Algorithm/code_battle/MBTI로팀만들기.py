def synergy(teams):
    global ans

    for team in teams:
        member_a, member_b = test_case[team[0]], test_case[team[1]]
        result = member_a[2] + member_b[2]
        n = 0
        if member_a[1] == 'O' or member_b[1] == 'O':
            result += 10
        if member_a[1] == member_b[1]:
            result -= 30
        if member_a[0][0] == 'E' and member_a[0][0] == member_b[0][0]:
            result += 40
        for t in range(4):
            if member_a[0][t] == member_b[0][t]:
                n += 1
        if n == 3:
            result += 40
        if result > ans[2]:
            ans = [team[0], team[1], result]


def make_teams(teams=[]):
    if len(teams) == N // 2:
        return synergy(teams)

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            member_a = test_case[i]
            team = [i]
            for j in range(1, N):
                if not visited[j]:
                    member_b = test_case[j]
                    if member_a[0] != member_b[0]:
                        if not (member_a[1] == 'O' and member_b[1] == 'O'):
                            if not (member_a[0][0] == 'I' and member_b[0][0] == 'I'):
                                if not (member_a[0][2] == 'T' and member_b[0][3] != 'P'):
                                    if not (member_a[0][3] != 'P' and member_b[0][2] == 'T'):
                                        visited[j] = True
                                        team.append(j)
                                        teams.append(team)
                                        make_teams(teams)
                                        teams.pop()
                                        team.pop()
                                        visited[j] = False
            visited[i] = False
            if len(team) == 1:
                return


T = int(input().strip())

for tc in range(1, T+1):
    N = int(input().strip())
    test_case = [list(input().strip().split()) for _ in range(N)]
    for t in range(N):
        test_case[t][2] = int(test_case[t][2])

    ans = [0, 0, 0]
    visited = [False] * N
    make_teams()
    ans.sort()
    if ans[2] == 0:
        print('#{} -1' .format(tc))
    else:
        print('#{} {} {} {}' .format(tc, ans[0]+1, ans[1]+1, ans[2]))