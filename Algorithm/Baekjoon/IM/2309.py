def my_sum(arr):
    sigma = 0
    for t in range(7):
        sigma += test_case[arr[t]]
    return sigma


def my_sort():
    for t_i in range(6):
        mini = t_i
        for t_j in range(t_i+1, 7):
            if test_case[temp[t_j]] < test_case[temp[mini]]:
                mini = t_j
        temp[t_i], temp[mini] = temp[mini], temp[t_i]


test_case = [int(input()) for _ in range(9)]

for i in range(1 << 9):
    temp = []
    for j in range(9):
        if i & (1 << j):
            temp.append(j)
    if len(temp) == 7:
        if my_sum(temp) == 100:
            my_sort()
            for idx in temp:
                print(test_case[idx])
            break
