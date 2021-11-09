def my_max():
    maxi = test_case[0]
    for t in test_case:
        if t > maxi:
            maxi = t

    return maxi


def my_avg():
    sigma = 0
    for t in temp:
        sigma += t

    return sigma / N


N = int(input().strip())
test_case = list(map(int, input().strip().split()))
maxi = my_max()
temp = []
for num in test_case:
    temp.append(num / maxi * 100)

print(my_avg())