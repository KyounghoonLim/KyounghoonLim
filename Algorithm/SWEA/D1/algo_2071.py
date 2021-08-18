def input_list():
    test = int(input('테스트 값을 입력하세요'))
    values = []
    for i in range(test):
        user_input = input('숫자 10가지를 입력하세요.')
        values += [list(map(int, user_input.split()))]

    return avg_values(values)

def avg_values(values):
    avg_list = []

    for i in values:
        tot = sum(i)
        avg = tot / len(i)
        avg_list.append(int(avg))

    return avg_list

print(input_list())



