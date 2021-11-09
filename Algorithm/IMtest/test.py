def volume(x, y):
    if x > y:
        a, b = x, y
    else:
        a, b = y, x
    h, maxi = 0, 0
    while True:
        temp = (a - h) * (b - h) * h / 2
        if b - h <= 0:
            break
        if temp > maxi:
            maxi = temp
        h += 0.0002

    return maxi


T = int(input().strip())

for tc in range(1, T + 1):
    test_case = list(map(int, input().strip().split()))

    x = test_case[0]
    y = test_case[1]

    print('#{} {:.6f}'.format(tc, volume(x, y)))
