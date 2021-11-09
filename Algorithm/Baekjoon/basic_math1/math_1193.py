test_case = int(input().strip())

p, temp = 0, 0
while test_case > temp:
    p += 1
    temp += p
n = temp - test_case
if p % 2:
    print('{}/{}' .format(n+1, p-n))
else:
    print('{}/{}' .format(p-n, n+1))