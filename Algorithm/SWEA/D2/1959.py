def my_max(arr):
    maxi = arr[0]
    for t in arr:
        if t > maxi:
            maxi = t

    return maxi


T = int(input().strip())

for tc in range(1, T+1):
    N, M = map(int, input().strip().split())
    A = list(map(int, input().strip().split()))
    B = list(map(int, input().strip().split()))
    if N > M:
        N, M = M, N
        A, B = B, A

    ans = []
    for i in range(M-N+1):
        temp = 0
        for j in range(N):
            temp += A[j] * B[j+i]
        ans.append(temp)

    print('#{} {}' .format(tc, my_max(ans)))