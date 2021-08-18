def input_list():
    test = int(input('테스트 값을 입력하세요'))
    values = []
    for i in range(test):
        user_input = input('숫자 10가지를 입력하세요.')
        values += [list(map(int, user_input.split()))]

    return odd_num_sigma(values)

def odd_num_sigma(values):
    ans = []
    for i in values:
        sigma = 0
        for j in i:
            if j % 2:
                sigma += j
        ans.append(sigma)

    return ans

print(input_list())