def my_bin(num, b_num=''):
    b_num = str(num % 2) + b_num
    if num // 2 == 0:
        return b_num
    elif num // 2 == 1:
        b_num = '1' + b_num
        return b_num
    num //= 2
    return my_bin(num, b_num)


T = int(input().strip())

for tc in range(1, T+1):
    test_case = input().strip()
    decoder = ''
    ans = ''
    p = 0
    while p < len(test_case):
        if 47 < ord(test_case[p]) < 58:
            temp = ord(test_case[p]) + 4
        if 64 < ord(test_case[p]) < 91:
            temp = ord(test_case[p]) - 65
        elif 96 < ord(test_case[p]) < 123:
            temp = ord(test_case[p]) - 71
        elif test_case[p] == '+':
            temp = 62
        elif test_case[p] == '/':
            temp = 63
        temp = my_bin(temp)
        if len(temp) < 6:
            for t in range(6-len(temp)):
                temp = '0' + temp
        decoder += temp
        if len(decoder) == 24:
            act = [decoder[:8], decoder[8:16], decoder[16:]]
            for i in range(3):
                ans += chr(int('0b' + act[i], 2))
            decoder = ''
        p += 1

    print('#{} {}' .format(tc, ans))