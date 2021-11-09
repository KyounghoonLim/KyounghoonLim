test_case = [list(map(int, input().strip().split())) for _ in range(4)]
paper = [[0] * 100 for _ in range(100)]
area = 0
for sq in test_case:
    for i in range(sq[1], sq[3]):
        for j in range(sq[0], sq[2]):
            if paper[i][j] == 0:
                paper[i][j] = 1
                area += 1

print(area)