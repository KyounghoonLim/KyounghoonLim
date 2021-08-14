T = int(input())
user_input = []
for test_case in range(1, T + 1):
    user_input.append(input())

for i in user_input:
    # result = ''
    if i[4:6] > '12' :
        result = '-1'
    elif int(i[4]) == 0 and int(i[5]) == 0:
        result = '-1'
    elif int(i[4]) == 0 and int(i[5]) == 2 :
        if int(i[6]) > 2 :
            result = '-1'
        elif int(i[6]) == 2 and int(i[7]) > 8 :
            result = '-1'
        else:
            year = i[0:4]
            month = i[4:6]
            date = i[6:8]
            result_list = [year, month, date]
            result = '/'.join(result_list)
    else:
        year = i[0:4]
        month = i[4:6]
        date = i[6:8]
        result_list = [year, month, date]
        result = '/'.join(result_list)
    print(result)


    
    