def reduce(x, y):
    if x > y and x % y == 0:
        x //= y
        y = 1
    elif x < y and y % x == 0:
        y //= x
        x = 1
    else:
        n = min((x, y))//2 + 1
        while (x > n and y > n) and n > 1:
            if x % n == 0 and y % n == 0:
                x //= n
                y //= n
            n -= 1

    return str(x), str(y)


T = int(input().strip())

for tc in range(1, T+1):
    test_case = input().strip()

    a, b = 1, 1
    for direc in test_case:
        if direc == 'L':
            b += a
        else:
            a += b

    # ans = reduce(a, b)

    print('#{} {} {}' .format(tc, a, b))