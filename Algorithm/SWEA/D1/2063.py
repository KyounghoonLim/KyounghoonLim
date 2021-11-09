def my_sort():
    for t_i in range(N - 1):
        mini = t_i
        for t_j in range(t_i + 1, N):
            if test_case[mini] > test_case[t_j]:
                mini = t_j
        test_case[t_i], test_case[mini] = test_case[mini], test_case[t_i]


def selection():
    for num in test_case:
        if num not in temp:
            temp.append(num)


N = int(input().strip())
test_case = list(map(int, input().strip().split()))
temp = []
my_sort()
selection()
print(temp[len(temp)//2+1])
