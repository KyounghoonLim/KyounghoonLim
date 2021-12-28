from itertools import combinations

test_case = input().strip().split()
N = len(test_case)

ans = []
for i in range(1, N):
    ans.extend(list(map(list, combinations(test_case, i))))

print(ans)