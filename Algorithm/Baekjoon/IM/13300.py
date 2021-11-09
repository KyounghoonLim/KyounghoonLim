N, K = map(int, input().strip().split())
test_case = [list(map(int, input().strip().split())) for _ in range(N)]
cnt = 0
boy = [0] * 7
girl = [0] * 7
for person in test_case:
    if person[0]:
        boy[person[1]] += 1
        if boy[person[1]] == K:
            cnt += 1
            boy[person[1]] = 0
    else:
        girl[person[1]] += 1
        if girl[person[1]] == K:
            cnt += 1
            girl[person[1]] = 0
for t in range(1, 7):
    if boy[t]:
        cnt += 1
        if girl[t]:
            cnt += 1
    elif girl[t]:
        cnt += 1

print(cnt)
