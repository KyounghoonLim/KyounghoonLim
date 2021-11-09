T = int(input())
user_input = []
for test_case in range(1, T + 1):
    user_input.append(input())

for i in range(len(user_input)):
    # result = ''
    if user_input[i][4:6] > '12' :
        result = '-1'
    elif int(user_input[i][4]) == 0 and int(user_input[i][5]) == 0:
        result = '-1'
    elif int(user_input[i][4]) == 0 and int(user_input[i][5]) == 2 :
        if int(user_input[i][6]) > 2 :
            result = '-1'
        elif int(user_input[i][6]) == 2 and int(user_input[i][7]) > 8 :
            result = '-1'
        else:
            year = user_input[i][0:4]
            month = user_input[i][4:6]
            date = user_input[i][6:8]
            result_list = [year, month, date]
            result = '/'.join(result_list)
    else:
        year = user_input[i][0:4]
        month = user_input[i][4:6]
        date = user_input[i][6:8]
        result_list = [year, month, date]
        result = '/'.join(result_list)
    print('#{} {}' .format(i + 1, result))
