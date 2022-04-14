T = int(input().strip())

for tc in range(1, T+1):
    P = input().strip()
    Q = input().strip()

    n, flag = 0, 0
    while n < len(P):
        p, q = ord(P[n]), ord(Q[n])
        if 65 <= p <= 90:
            p += 58
        if 65 <= q <= 90:
            q += 58
        print(p, q)
        if n == q:
            print('#{} N' .format(tc))
            flag = 1
            break
        if p < q:
            print('#{} Y' .format(tc))
            flag = 1
            break
        elif p > q:
            print('#{} N' .format(tc))
            flag = 1
            break
        n += 1
    if not flag:
        if (len(P) < len(Q) and Q[n] == 'a') or (len(P) == len(Q)):
            print('#{} N' .format(tc))
        else:
            print('#{} Y' .format(tc))