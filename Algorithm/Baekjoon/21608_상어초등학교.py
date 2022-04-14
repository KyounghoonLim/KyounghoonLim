di = [-1, 0 ,1, 0]
dj = [0, 1, 0, -1]


def find_sit(student):
    likes = []
    for i in range(N):
        for j in range(N):
            if not table[i][j]:
                like_one = [i, j, 0, 0]
                for t in range(4):
                    ti, tj = i + di[t], j + dj[t]
                    if 0 <= ti < N and 0 <= tj < N:
                        if not table[ti][tj]:
                            like_one[3] -= 1
                        if table[ti][tj] in student[1:]:
                            like_one[2] -= 1
                likes.append(like_one)
    likes.sort(key=lambda x:(x[2], x[3], x[0], x[1]))
    table[likes[0][0]][likes[0][1]] = student[0]

    return


N = int(input().strip())
test_case = [list(map(int, input().strip().split())) for _ in range(N**2)]
table = [[0] * N for _ in range(N)]
table_likes = [[0] * N for _ in range(N)]

for idx in range(N**2):
    find_sit(test_case[idx])

test_case.sort()

ans = 0
for y in range(N):
    for x in range(N):
        sigma = 0
        for t in range(4):
            ti, tj = y + di[t], x + dj[t]
            if 0 <= ti < N and 0 <= tj < N:
                if table[ti][tj] in test_case[table[y][x]-1]:
                    sigma += 1
        if sigma:
            ans += 10 ** (sigma-1)

print(ans)