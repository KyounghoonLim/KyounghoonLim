test_case = list(map(int, input().strip().split()))
ans = 0
if test_case[1] >= test_case[2]:
    ans = -1
else:
    ans += test_case[0] // (test_case[2] - test_case[1]) + 1

print(ans)