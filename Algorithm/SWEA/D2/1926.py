test_case = int(input().strip())
ans = ''

for i in range(1, test_case + 1):
    cnt = 0
    for t in str(i):
        if int(t) != 0 and int(t) % 3 == 0:
            cnt += 1
    if cnt:
        ans += '-' * cnt
    else:
        ans += str(i)
    ans += ' '

print(ans)
