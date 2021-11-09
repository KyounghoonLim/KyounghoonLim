test_case = int(input().strip())
n = len(str(test_case))
flag = 0
s = test_case - 9 * n
if s < 0:
    s = 1
for i in range(s, test_case):
    ans = i
    for j in str(i):
        ans += int(j)
    if ans == test_case:
        print(i)
        flag = 1
        break
if not flag:
    print(0)