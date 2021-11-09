def hansoo(n):
    num = str(n)
    flag, gap = 0, 0
    for t in range(len(num)-1):
        if flag:
            if int(num[t]) + gap != int(num[t+1]):
                return
        else:
            gap = int(num[t+1]) - int(num[t])
            flag = 1

    return True


test_case = int(input().strip())
ans = 0
for i in range(1, test_case+1):
    if hansoo(i):
        ans += 1

print(ans)