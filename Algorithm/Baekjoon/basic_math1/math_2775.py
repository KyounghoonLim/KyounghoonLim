T = int(input().strip())

for tc in range(T):
    k = int(input().strip())
    n = int(input().strip())
    temp = [[], []]
    f = 0
    while f < k+1:
        for num in range(1,n+1):
            if f == 0:
                temp[0].append(num)
            else:
                sigma = 0
                for i in range(num):
                    sigma += temp[0][i]
                temp[1].append(sigma)
        f += 1
        if f != 1:
            temp.pop(0)
            temp.append([])
    print(temp[0][n-1])