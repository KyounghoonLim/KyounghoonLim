x, y = map(int, input().strip())
N = int(input().strip())
test_case = [list(map(int, input().strip().split())) for _ in range(N-1)]
d, r = map(int, input().strip().split())
sigma = 0
for shop in test_case:
    if shop[0] == d:
        sigma += abs(r-shop[1])
    elif abs(shop[0] - d) == 1:
        if shop[0] == 3:
            sigma += y - shop[1] + r
        else:
            sigma += y - r + shop[1]
    elif abs(shop[0] - d) == 2:
        