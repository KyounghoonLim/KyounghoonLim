T = int(input().strip())
result = []
for tc in range(T):
    test_case = int(input().strip())
    sigma = 0
    for i in range(1, test_case + 1):
        if i % 2:
            sigma += i
        else:
            sigma -= i
    result.append(sigma)
for i in range(len(result)):
    print('#{} {}' .format(i+1, result[i]))