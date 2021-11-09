N = int(input().strip())
max_len = 0
ans = []
for num in range(N//2, N+1):
    temp = [N]
    temp.append(num)
    i = 0
    while temp[i] - temp[i+1] >= 0:
        temp.append(temp[i] - temp[i+1])
        i += 1
    if len(temp) > max_len:
        max_len = len(temp)
        ans = temp[:]

print(max_len)
for t in ans:
    print(t, end=' ')