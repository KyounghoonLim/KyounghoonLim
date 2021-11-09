test_case = int(input().strip())
ans = []
num, s = test_case, 2
while num > 1:
    if num % s == 0:
        num //= s
        ans.append(s)
    else:
        s += 1

for i in ans:
    print(i)