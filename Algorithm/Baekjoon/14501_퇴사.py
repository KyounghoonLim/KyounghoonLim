def counseling(idx=0, pay=0):
    global ans

    for i in range(idx, N):
        if i + test_case[i][0] < N+1:
            counseling(i + test_case[i][0], pay + test_case[i][1])
    if ans < pay:
        ans = pay
    return


N = int(input().strip())

test_case = [list(map(int, input().strip().split())) for _ in range(N)]

ans = 0
counseling()
print(ans)