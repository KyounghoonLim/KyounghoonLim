def my_sum(arr):
    sigma = 0
    for t in arr:
        sigma += t

    return sigma


N, M = map(int, input().strip().split())
test_case = list(map(int, input().strip().split()))
maxi = 0
for i in range(N-2):
    if test_case[i] > M:
        continue
    for j in range(i+1, N-1):
        if test_case[i] + test_case[j] > M:
            continue
        for k in range(j+1, N):
            if maxi < test_case[i] + test_case[j] + test_case[k] <= M:
                maxi = test_case[i] + test_case[j] + test_case[k]

print(maxi)
