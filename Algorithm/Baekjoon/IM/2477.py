N = int(input().strip())
test_case = [list(map(int, input().strip().split())) for _ in range(6)]
cnt = [0]*5
line = []
for i in range(6):
    cnt[test_case[i][0]] += 1
    line.append([test_case[i][1], i])