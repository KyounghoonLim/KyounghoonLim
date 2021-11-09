def my_max():
    maxi = test_case[0]
    if test_case[1] > maxi:
        print(test_case[1])
    else:
        print(maxi)


test_case = list(map(int, input().strip().split()))

for n in range(2):
    temp = 0
    i = 2
    while test_case[n] > 0:
        temp += (test_case[n] % 10) * (10 ** i)
        test_case[n] //= 10
        i -= 1
    test_case[n] = temp
my_max()