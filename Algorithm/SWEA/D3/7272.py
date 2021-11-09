def is_same_word(a, b):
    z_h = 'CEFGHIJKLMNSTUVWXYZ'
    o_h = 'ADOPQR'
    if a in z_h:
        if b in z_h:
            return True
        else:
            return False
    if a in o_h:
        if b in o_h:
            return True
        else:
            return False
    if a == 'B' and a == b:
        return True


def comparing(a, b):
    if len(a) != len(b):
        print('#{} DIFF'. format(tc))
        return
    for i in range(len(a)):
        if not is_same_word(a[i], b[i]):
            print('#{} DIFF' .format(tc))
            return
    print('#{} SAME' .format(tc))


T = int(input().strip())

for tc in range(1, T+1):
    test_case = input().strip().split()

    comparing(test_case[0], test_case[1])