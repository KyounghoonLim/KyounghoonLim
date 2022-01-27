di = [0, -1, 0, 1]
dj = [1, 0, -1, 0]


def dragon_curve(st, dragon, g=0):
    if not paper[st[1]][st[0]]:
        paper[st[1]][st[0]] = 1
    temp = dragon.copy()
    for idx in range(len(dragon)):
        d = dragon[idx]
        x, y = st[0] + dj[d], st[1] + di[d]
        if 0 <= x <= 100 and 0 <= y <= 100:
            paper[y][x] = 1
            st = [x, y]
            if g:
                temp = [(d + 1) % 4] + temp
            else:
                temp[idx] = (d + 1) % 4
        else:
            return
    if g < target:
        dragon_curve(st, temp, g+1)


N = int(input().strip())
test_case = [list(map(int, input().strip().split())) for _ in range(N)]
paper = [[0] * 101 for _ in range(101)]

for case in test_case:
    target = case[3]
    dragon_curve([case[0], case[1]], [case[2]])

ans = 0

for i in range(100):
    for j in range(100):
        if paper[i][j] and paper[i+1][j] and\
            paper[i][j+1] and paper[i+1][j+1]:
            ans += 1

print(ans)