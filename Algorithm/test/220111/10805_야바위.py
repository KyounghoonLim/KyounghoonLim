T = int(input().strip())

for tc in range(1, T+1):
    N, Q = map(int, input().strip().split())
    test_case = [list(map(int, input().strip().split())) for _ in range(Q)]

    ans = [False] * N
    result = [[False, False] for _ in range(Q)]
    n = Q
    # while n > 0:
        

    print('#{} {}' .format(tc, ans.count(True)))