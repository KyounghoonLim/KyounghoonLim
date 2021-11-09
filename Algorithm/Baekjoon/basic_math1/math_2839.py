test_case = int(input().strip())
temp = test_case

if temp >= 5:
    ans = temp // 5
    temp %= 5
    while temp > 0:
        if temp > test_case:
            ans = -1
            break
        if temp % 3:
            temp += 5
            ans -= 1
        else:
            ans += temp // 3
            temp = 0
else:
    if temp == 3:
        ans = 1
    else:
        ans = -1

print(ans)