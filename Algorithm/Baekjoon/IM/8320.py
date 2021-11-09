N = int(input().strip())
cnt = 0
for i in range(1, N//2):
    if i ** 2 <= N:
        for t in range(i**2, N+1, i):
            cnt += 1

print(cnt)