def is_num(num):
    remain = num // 2
    count = 0
    for i in range(1,remain+1):
        if num % remain:
            continue
        else:
            count += 1
    if count < 2:
        return print('소수입니다.')
    else:
        return print('소수가 아닙니다.')

is_num(13)