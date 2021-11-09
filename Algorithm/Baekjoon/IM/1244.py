def switch_boy(num: int):
    t_num = num
    while t_num < N-1:
        test_case[num - 1] = 1 - test_case[num - 1]
        num += t_num


def switch_girl(num: int):
    t = 1
    test_case[num] = 1 - test_case[num]
    while True:
        if 0 <= num - t and num + t < N and test_case[num - t] == test_case[num + t]:
            test_case[num - t] = 1 - test_case[num - t]
            test_case[num + t] = 1 - test_case[num + t]
        else:
            break
        t += 1


N = int(input().strip())
test_case = list(map(int, input().strip().split()))
M = int(input().strip())
student = [list(map(int, input().strip().split())) for _ in range(M)]

for i in range(M):
    person = student.pop(0)
    if person[0] == 1:
        switch_boy(person[1])
    else:
        switch_girl(person[1]-1)

for i in range(N):
    if i != 0 and i % 20 == 0:
        print()
    print(test_case[i], end=' ')
