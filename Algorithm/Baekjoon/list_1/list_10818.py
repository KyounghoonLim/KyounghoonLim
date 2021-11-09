N = int(input().strip())
test_case = list(map(int, input().strip().split()))

maxi = test_case[0]
mini = test_case[0]
for i in range(1, N):
    if test_case[i] > maxi:
        maxi = test_case[i]
    if test_case[i] < mini:
        mini = test_case[i]

print(mini, maxi)