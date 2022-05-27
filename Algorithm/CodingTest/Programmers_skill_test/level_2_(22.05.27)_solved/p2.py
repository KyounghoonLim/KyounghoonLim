di = [1, 0, -1]
dj = [0, 1, -1]


def solution(n):
    answer = []

    test_case = []
    for i in range(n):
        test_case.append([0] * (i+1))

    num = 1; d = 0
    i, j = -1, 0
    flag = 0
    while True:
        try:
            if flag == 3:
                break
            elif test_case[i + di[d]][j + dj[d]] == 0:
                test_case[i + di[d]][j + dj[d]] = num
                num += 1
                flag = 0
                i, j = i + di[d], j + dj[d]
            else:
                raise ValueError
        except:
            d = (d + 1) % 3
            flag += 1

    for k in range(n):
        answer.extend(test_case[k])


    return answer

print(solution(5))