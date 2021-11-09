test_case = list(map(int, input().strip().split()))

win = test_case[0] - test_case[1]
if win == 1:
    print('A')
elif win == -1:
    print('B')
elif win == 2:
    print('B')
else:
    print('A')
