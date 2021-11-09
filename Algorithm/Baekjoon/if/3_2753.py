test_case = int(input().strip())
a = test_case % 4
b = test_case % 100
c = test_case % 400
if test_case % 4 == 0 and (test_case % 100 or test_case % 400 == 0):
    print(1)
else:
    print(0)