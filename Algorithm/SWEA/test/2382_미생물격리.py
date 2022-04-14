di = [0, -1, 1, 0, 0]
dj = [0, 0, 0, -1, 1]

T = int(input().strip())

for tc in range(1, T + 1):
    N, M, K = map(int, input().strip().split())
    cells = []
    for t in range(K):
        cells.append(list(map(int, input().strip().split())))

    ans2 = 0
    for cell in cells:
        ans2 += cell[2]
    print(ans2)
    while M > 0:
        for cell in cells:
            if cell[2]:
                cell[0], cell[1] = cell[0] + di[cell[3]], cell[1] + dj[cell[3]]
                if cell[0] == 0 or cell[0] == N+1 or cell[1] == 0 or cell[1] == N+1:
                    cell[2] //= 2
                    if cell[3] % 2:
                        cell[3] += 1
                    else:
                        cell[3] -= 1

        result = []
        visited = [0] * len(cells)
        for i in range(len(cells)):
            if not visited[i] and cells[i][2]:
                maxi = i
                nums_of_cells = 0
                for j in range(i, len(cells)):
                    if cells[i][0] == cells[j][0] and cells[i][1] == cells[j][1]:
                        visited[j] = 1
                        nums_of_cells += cells[j][2]
                        if cells[maxi][2] < cells[j][2]:
                            maxi = j
                result.append([cells[i][0], cells[i][1], nums_of_cells, cells[maxi][3]])
        cells = result
        M -= 1
    ans = 0
    for cell in cells:
        ans += cell[2]

    print('#{} {}' .format(tc, ans))