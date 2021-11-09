def is_prime(num):
    for t in range(2, int(num ** 0.5) + 1):
        if num % t == 0:
            return

    return True


T = int(input().strip())

for tc in range(T):
    test_case = int(input().strip())
    prime = []
    for n in range(2, test_case+1):
        if is_prime(n):
            prime.append(n)
    temp = []
    for i in prime:
        for j in prime:
            if i + j == test_case:
                temp.append([i, j, abs(i-j)])

    mini = 0
    for i in range(len(temp)):
        if temp[i][2] < temp[mini][2]:
            mini = i
    print(temp[mini][0], temp[mini][1])