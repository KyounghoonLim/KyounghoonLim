user_input = input()
ans_list = []

for i in range(1, int(user_input)+1):
    temp = ''
    if i % 3 > 0:
        for j in range(1, len(str(i))):
            if int(str(i)[0:-1]) % 3 > 0:
                temp += str(i)
            else:
                temp += '-'
    else:
        temp += '-'
        for j in range(1, len(str(i))):
            if i[0:-1] % 3 == 0:
                temp += '-'
            else:
                continue

    ans_list.append(temp)

ans = ' '.join(ans_list)
print(ans)