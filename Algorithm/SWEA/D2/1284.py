T = int(input().strip())

for tc in range(1, T+1):
    a, b, R, S, W = map(int, input().strip().split())
    A = a * W
    if W <= R:
        B = b
    else:
        B = b + (W - R) * S
    if A > B:
        print('#{} {}' .format(tc, B))
    else:
        print('#{} {}' .format(tc, A))