def attach(j, i):
    for t_i in range(50-10-i, 50-i):
        for t_j in range(j, 10+j):
            if t_i == 50-10-i or t_i == 49-i:
                paper[t_i][t_j] += 1
            elif t_j == j or t_j == 9+j:
                paper[t_i][t_j] += 1
            else:
                paper[t_i][t_j] += 2


N = int(input().strip())
test_case = [list(map(int, input().strip().split())) for _ in range(N)]
paper = [[0]*50 for _ in range(50)]
for bk in test_case:
    attach(bk[0], bk[1])
cnt = 0
for i in range(50):
    for j in range(50):
        if paper[i][j] == 1:
            cnt += 1
for i in paper:
    print(i)


print(cnt)