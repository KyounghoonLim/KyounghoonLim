def is_poss():
    if N >= 100:
        return True
    elif N == 0 and D:
        return False
    else:
        if not N % 2:
            for t1 in range(N, 0, -1):
                for t2 in range(t1, -1, -1):
                    if abs((t2/t1) * 100 - D) < 1 ** (-24):
                        return True
        return False


T = int(input().strip())

for tc in range(1, T+1):
    N, D, G = map(int, input().strip().split())
    if is_poss():
        if D == G or (D != G and (G != 100 and G != 0)):
            print('#{} Possible' .format(tc))
            continue
    print('#{} Broken'.format(tc))