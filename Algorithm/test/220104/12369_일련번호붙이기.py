T = int(input().strip())

for tc in range(1, T + 1):
    test_case = input().strip().split()
    S, N = test_case[0], int(test_case[1])
    i = 1
    temp = []
    while True:
        temp.append(len(S) ** i)
        if sum(temp) > N:
            break
        i += 1

    result = [0] * i
    num = N - sum(temp[:-1])
    for idx in range(i):
        for n in range(1, i):
            if num <= len(S) ** (i - idx - 1) * n:
                result[idx] = n
                if idx == i - 1 and num == len(S) ** (i - idx - 1) * n:
                    num = 0
                else:
                    num -= len(S) ** (i - idx - 1) * (n - 1)
                break
    if num:
        result[-1] = num
    ans = ''
    for t in result:
        ans += S[t-1]
    print('#{} {}' .format(tc, ans))