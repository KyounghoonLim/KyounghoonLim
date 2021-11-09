N, K = map(int, input().strip().split())
test_case = list(map(int, input().strip().split()))
maxi = -99999999
sigma = 0
for i in range(N-K+1):
    if i == 0:
        for k in range(K):
            sigma += test_case[i+k]
    else:
        sigma -= test_case[i-1]
        sigma += test_case[i+K-1]
    if sigma > maxi:
        maxi = sigma

print(maxi)