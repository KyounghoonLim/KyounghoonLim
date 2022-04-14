N, M = map(int, input().split())
test_cast = []

R, B = False, False

for i in range(N):
    temp = input()
    arr = []
    for j in range(M):
        if temp[j] == 'R':
            R = (i, j)
            arr.append('.')
        elif temp[j] == 'B':
            B = (i, j)
            arr.append('.')
        else:
            arr.append(temp[j])
    test_cast.append(arr)


di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def escape(r, b, n=1, before=-1):
    global ans

    if n == 11:
        return
    elif ans == -1 or n < ans:
        for t in range(4):
            if t == before:
                continue
            balls = []
            flag = 0
            for ball in [r, b]:
                for c in range(0, 8):
                    if test_cast[ball[0] + di[t] * c][ball[1] + dj[t] * c] == 'O':
                        if ball == r:
                            flag = n
                            break
                        elif ball == b:
                            flag = 0
                            break
                    elif test_cast[ball[0] + (di[t] * c) + di[t]][ball[1] + (dj[t] * c) + dj[t]] == '#':
                        if test_cast[ball[0] + di[t] * c][ball[1] + dj[t] * c] == '.':
                            balls.append([ball[0] + di[t] * c, ball[1] + dj[t] * c, c])
                            break
            if flag:
                if ans == -1 or ans > flag:
                    ans = flag
            elif len(balls) == 2:
                if balls[0][0] == balls[1][0] and balls[0][1] == balls[1][1]:
                    if balls[0][2] > balls[1][2]:
                        if t == 0 or t == 2:
                            balls[0][0] = balls[0][0] - di[t]
                        else:
                            balls[0][1] = balls[0][1] - dj[t]
                    else:
                        if t == 0 or t == 2:
                            balls[1][0] = balls[1][0] - di[t]
                        else:
                            balls[1][1] = balls[1][1] - dj[t]
                escape(balls[0], balls[1], n+1, t)


ans = -1
log = []
escape(R, B)

print(ans)