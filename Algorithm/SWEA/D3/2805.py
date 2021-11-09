T = int(input().strip())

for tc in range(1, T + 1):
    N = int(input().strip())
    test_case = [list(map(int, input().strip())) for _ in range(N)]
    mid = N // 2    #중간값 지정
    ans = 0 #각 수확물의 합
    for i in range(mid+1):  #중간지점 까지
        for j in range(mid - i, mid + 1 + i):
            ans += test_case[i][j]
    for i in range(mid+1, N):   #중간지점부터
        for j in range(mid - (N - 1 - i), mid + 1 + (N - 1 - i)):
            ans += test_case[i][j]

    print('#{} {}' .format(tc, ans))