T = int(input().strip())

for tc in range(1, T+1):
    test_case = input().strip()

    cnt = [0] * 26
    for word in test_case:
        cnt[int(ord(word))-97] += 1

    ans = ''
    for t in range(26):
        if cnt[t] and cnt[t] % 2:
            ans += chr(t+97)
    if ans:
        print('#{} {}' .format(tc ,ans))
    else:
        print('#{} GOOD' .format(tc))
