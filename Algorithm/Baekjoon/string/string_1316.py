def is_group(txt):
    for t in range(len(txt)):
        if t == 0:
            temp[ord(txt[t])-97] = 1
        elif temp[ord(txt[t])-97] == 0:
            temp[ord(txt[t])-97] = 1
        else:
            if txt[t] != txt[t-1]:
                return
    return True


N = int(input().strip())
test_case = [input().strip() for _ in range(N)]

ans = 0
for text in test_case:
    temp = [0] * 26
    if is_group(text):
        ans += 1

print(ans)