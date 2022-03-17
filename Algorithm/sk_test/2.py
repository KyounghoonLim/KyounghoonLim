import pprint

def solution(n, clockwise):
    answer = [[0] * n for _ in range(n)]

    st = [[0, 0], [0, n-1], [n-1, n-1], [n-1, 0]]
    num = 1
    d = 0
    while True:
        if clockwise:
            di = [0, 1, 0, -1]
            dj = [1, 0, -1, 0]
            for i in range(4):
                answer[st[i][0]][st[i][1]] = num
                if not i and answer[st[i][0] + di[(i+d) % 4]][st[i][1] + dj[(i+d) % 4]]:
                    d += 1
                st[i][0] += di[(i+d) % 4]
                st[i][1] += dj[(i+d) % 4]
        else:
            di = [1, 0, -1, 0]
            dj = [0, -1, 0, 1]
            for i in range(4):
                answer[st[i][0]][st[i][1]] = num
                if not i and answer[st[i][0] + di[(i - d) % 4]][st[i][1] + dj[(i - d) % 4]]:
                    d += 1
                st[i][0] += di[(i - d) % 4]
                st[i][1] += dj[(i - d) % 4]
        if answer[st[3][0]][st[3][1]]:
            break
        num += 1

    return answer

pprint.pp(solution(4, True))