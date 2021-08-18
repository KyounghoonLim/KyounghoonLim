T = int(input())
user_input = []
for test_case in range(1, T + 1):
    user_input += [input().split()]

count = 0
for i in user_input:
    result = ''
    if i[0] > i[1]:
        count += 1
        result += '>'
    elif i[0] < i[1]:
        count += 1
        result += '<'
    else:
        count += 1
        result += '='
    print(f'#{count} {result}')