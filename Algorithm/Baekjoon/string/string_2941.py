def is_in(txt):
    for t in range(8):
        if txt == c_alpha[t]:
            return True


c_alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
test_case = input().strip()

i, cnt = 0, 0
while i < len(test_case):
    temp = test_case[i:i+2]
    if is_in(temp):
        i += 2
    else:
        temp = test_case[i:i+3]
        if is_in(temp):
            i += 3
        else:
            i += 1
    cnt += 1

print(cnt)