user_input = []
input_dict = {}
for i in range(4):
    user_input.append(input())

for i in range(2):
    input_dict[user_input[i]] = user_input[i+2]

result_list = list(input_dict.keys())

if input_dict[result_list[0]] == '가위':
    if input_dict[result_list[1]] == '가위':
        print('무승부')
    elif input_dict[result_list[1]] == '바위':
        print('바위가 이겼습니다!')
    else:
        print('가위가 이겼습니다!')
if input_dict[result_list[0]] == '바위':
    if input_dict[result_list[1]] == '가위':
        print('바위가 이겼습니다.')
    elif input_dict[result_list[1]] == '바위':
        print('무승부')
    else:
        print('보가 이겼습니다!')
if input_dict[result_list[0]] == '보':
    if input_dict[result_list[1]] == '가위':
        print('가위가 이겼습니다!')
    elif input_dict[result_list[1]] == '바위':
        print('보가 이겼습니다!')
    else:
        print('무승부')