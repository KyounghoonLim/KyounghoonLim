T = int(input().strip())
result = []

for tc in range(T):
    test_case = list(map(int, input().strip().split()))

    for i in range(len(test_case)-1):
        for j in range(i + 1, len(test_case)):
            if test_case[i] > test_case[j]:
                temp = test_case[i]
                test_case[i] = test_case[j]
                test_case[j] = temp

    mini = test_case[0]
    maxi = test_case[-1]
    for k in range(len(test_case)-1, -1, -1):
        if test_case[k] == mini:
            test_case.pop(k)
        elif test_case[k] == maxi:
            test_case.pop(k)

    sigma = 0
    for l in test_case:
        sigma += l
    result.append(round(sigma/len(test_case)))

for i in range(len(result)):
    print('#{} {}' .format(i+1, result[i]))