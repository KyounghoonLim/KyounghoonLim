T  = int(input())
user_input = []
for tc in range(T):
    user_input.append(input().rstrip())

palindrome_list = []
for text in user_input:
    temp = []
    for i in range(len(text)-1, -1, -1):
        temp.append(text[i])
    palindrome = ''.join(temp)
    palindrome_list.append(palindrome)

for i in range(len(user_input)):
    if user_input[i] == palindrome_list[i]:
        print('#{} 1' .format(i+1))
    else:
        print('#{} 0' .format(i+1))

