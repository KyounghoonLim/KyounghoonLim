test_case = [int(input().strip()) for _ in range(9)]
maxi = 0
for i in range(1, 9):
    if test_case[i] > test_case[maxi]:
        maxi = i

print(test_case[maxi])
print(maxi+1)