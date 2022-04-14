def calculation(calculator, result, n=0):
    global max_ans, min_ans

    if n == N - 1:
        if result >= max_ans:
            max_ans = result
        if result <= min_ans:
            min_ans = result
        return

    for j in range(4):
        if calculator[j]:
            calculator[j] -= 1
            if j == 0:
                temp = result + test_case[n+1]
            elif j == 1:
                temp = result - test_case[n+1]
            elif j == 2:
                temp = result * test_case[n+1]
            else:
                temp = result // test_case[n+1]
                if result < 0:
                    temp = (abs(result) // test_case[n+1]) * (-1)
            calculation(calculator, temp, n+1)
            calculator[j] += 1


N = int(input().strip())
test_case = list(map(int, input().strip().split()))
calc = list(map(int, input().strip().split()))

max_ans = -1000000000
min_ans = 1000000000
calculation(calc, test_case[0])

print(max_ans)
print(min_ans)