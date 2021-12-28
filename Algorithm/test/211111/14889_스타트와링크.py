def team_synergy(team):
    sigma = 0
    for t1 in range(N):
        if chosen[t1] == team:
            for t2 in range(N):
                if chosen[t2] == team:
                    sigma += test_case[t1][t2]

    return sigma


def make_team(n=0, total=0, member=0):
    global ans

    if member == N//2:
        sub_synergy = abs(total - team_synergy(False))
        if ans > sub_synergy:
            ans = sub_synergy
        return

    if n >= N:
        return

    if n == 0:
        chosen[n] = True
        make_team(n+1, 0, 1)
    else:
        for t in range(n, N):
            if not chosen[t]:
                chosen[t] = True
                total_synergy = team_synergy(True)
                make_team(t+1, total_synergy, member+1)
                chosen[t] = False


N = int(input().strip())
test_case = [list(map(int, input().strip().split())) for _ in range(N)]

chosen = [False] * N

ans = 999999999
make_team()

print(ans)