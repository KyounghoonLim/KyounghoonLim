def is_complete(arr):
    for t in range(N):



N, L = map(int, input().strip().split())
test_case = [list(map(int, input().strip().split())) for _ in range(N)]
record = [[False] * N for _ in range(N)]

for i in range(N):
    for j in range(N-1):
        if test_case[i][j] * L == sum(test_case[i][j:j+L]):
            try:
                record[i][j:j+L].index(True)
            except:
                if j < N - L - 1 and test_case[i][j] + 1 == test_case[i][j+L+1]:
                    for t in range(L):
                        record[i][j+t] = True
    for k in range(N-1, 1, -1):
        if test_case[i][k] * L == sum(test_case[i][k-L+1:k+1]):
            try:
                record[i][k-L:k].index(True)
            except:
                if k > 0 and test_case[i][k] + 1 == test_case[i][k-L-1]:
                    for t in range(L):
                        record[i][k-t] = True

print(record)


# N, L = map(int, input().strip().split())
# test_case = [list(map(int, input().strip().split())) for _ in range(N)]
# record = [[False] * N for _ in range(N)]
#
# for i in range(N):
#     for j in range(N-L):
#         if test_case[i][j] * L == sum(test_case[i][j:j+L]):
#             for t in range(L):
#                 record[i][j+t] = True
#         sigma = 0
#         for k in range(L):
#             sigma += test_case[j+k][i]
#         if test_case[j][i] * L == sigma:
#             for t in range(L):
#                 record[j+t][i] = True
#
# print(record)