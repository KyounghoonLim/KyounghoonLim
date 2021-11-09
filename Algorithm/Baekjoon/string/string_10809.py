test_case = input().strip()

for n in range(97, 123):
    flag = 0
    for i in range(len(test_case)):
        if n == ord(test_case[i]):
            print(i, end=' ')
            flag = 1
            break
    if not flag:
        print(-1, end=' ')