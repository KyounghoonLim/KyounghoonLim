import sys
sys.setrecursionlimit(1000000)


def find_rear(rear):
    test_case[rear[0]][rear[1]] = 0
    for d in range(4):
        i, j = rear[0] + di[d], rear[1] + dj[d]
        if 0 <= i < N and 0 <= j < N and test_case[i][j] == 1:
            if visited[i][j] - visited[rear[0]][rear[1]] == 1:
                return (i, j)


def dummy(head, rear, d=1, s=1):
    i, j = head[0] + di[d], head[1] + dj[d]

    if 0 <= i < N and 0 <= j < N and test_case[i][j] != 1:
        visited[i][j] = s
        flag = False
        if test_case[i][j] == 2:
            flag = True
        test_case[i][j] = 1
        head = (i, j)
        if not flag:
            rear = find_rear(rear)

        if str(s) in moves.keys():
            move = moves[str(s)]
            if move == 'D':
                d = (d + 1) % 4
            else:
                d = (d - 1) % 4
        return dummy(head, rear, d, s+1)
    else:
        return s


N = int(input())
test_case = [[0] * N for _ in range(N)]
test_case[0][0] = 1

for _ in range(int(input())):
    i, j = map(int, input().split())
    test_case[i-1][j-1] = 2

moves = {}

for _ in range(int(input())):
    second, direction = input().split()
    moves[second] = direction

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

visited = [[0] * N for _ in range(N)]

print(dummy(head=(0, 0), rear=(0, 0)))