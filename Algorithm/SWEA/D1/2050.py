user_input = input()
ans_list = []
for i in user_input:
    if ord(i) > 64 and ord(i) < 91: 
        ans_list.append(str(ord(i)-64))
    elif ord(i) > 96 and ord(i) < 123:
        ans_list.append(str(ord(i)-96))
    else:
        print('알파벳을 입력해주세요.')

ans = ' '.join(ans_list)

print(ans)