def remover(n=0):
    if 3 ** n >= test_case:
        return
    for ti in range(3 ** n, test_case, 3 ** (n + 1)):
        for tj in range(3 ** n, test_case, 3 ** (n + 1)):
            star[ti][tj] = ' '
            if n:
                for ti_2 in range(ti, ti + 3 ** n):
                    for tj_2 in range(tj, tj + 3 ** n):
                        star[ti_2][tj_2] = ' '

    remover(n + 1)


test_case = int(input().strip())
star = [['*'] * test_case for _ in range(test_case)]
remover()
for si in range(test_case):
    for sj in range(test_case):
        print(star[si][sj], end='')
    print()
