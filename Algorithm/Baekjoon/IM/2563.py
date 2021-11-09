def attach(j, i):
    global cnt
    for t_i in range(100-10-i, 100-i):
        for t_j in range(j, 10+j):
            paper[t_i][t_j] += 1
            if paper[t_i][t_j] == 1:
                cnt += 1


N = int(input().strip())
test_case = [list(map(int, input().strip().split())) for _ in range(N)]
paper = [[0]*100 for _ in range(100)]
cnt = 0
for bk in test_case:
    attach(bk[0], bk[1])

print(cnt)