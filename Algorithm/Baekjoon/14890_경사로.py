def return_road(target, n):
    for tar in target:
        if visited[tar[0]][tar[1]] == n:
            visited[tar[0]][tar[1]] = 0


def make_road(road, n):
    global ans

    temp = [1] * N
    for k in range(1, N):
        result = abs(test_case[road[k][0]][road[k][1]] - test_case[road[k-1][0]][road[k-1][1]])
        if result > 1:  ### 높이 검증 ###
            return False
        elif result == 0:   ### 연속성 체크 ###
            temp[k] += temp[k-1]
            for l in range(k-1, k-temp[k], -1):
                temp[l] = temp[k]

    for t in range(N-1):  ### 연속성 검증 ###
        result = test_case[road[t][0]][road[t][1]] - test_case[road[t+1][0]][road[t+1][1]]
        if result == 0:
            continue
        elif result == 1 and temp[t+1] >= L:  ### 오른쪽 검증 ###
            for tar in range(t+1, t+L+1):
                if tar >= N or visited[road[tar][0]][road[tar][1]] == n:    ### 길이 검증 및 경사로 유무 검증 ###
                    return return_road(road, n)
                else:
                    visited[road[tar][0]][road[tar][1]] = n ### 경사로 쌓기 ###
        elif result == -1 and temp[t] >= L: ### 왼쪽 검증 ###
            for tar in range(t, t-L, -1):
                if tar < 0 or visited[road[tar][0]][road[tar][1]] == n:    ### 길이 검증 및 경사로 유무 검증 ###
                    return return_road(road, n)
                else:
                    visited[road[tar][0]][road[tar][1]] = n ### 경사로 쌓기 ###
        else:
            return False

    ans += 1    ### 모든 검증 통과시 ###


N, L = map(int, input().split())
test_case = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

ans = 0

for i in range(N):
    h_road, v_road = [], []
    for j in range(N):
        h_road.append([i, j])
        v_road.append([j, i])
    make_road(h_road, f'h-{i + 1}')
    make_road(v_road, f'v-{i + 1}')

print(ans)