T = int(input().strip())

for tc in range(1, T+1):
    D, L, N = map(int, input().strip().split())

    damage = 0
    for n in range(N):
        damage += D * (1 + n * L / 100)

    print('#{} {:.0f}' .format(tc, damage))