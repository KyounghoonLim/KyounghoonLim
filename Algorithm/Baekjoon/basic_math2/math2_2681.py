def is_prime(num):
    for t in range(2, num//2 + 1):
        if num % t == 0:
            return

    return True


M = int(input().strip())
N = int(input().strip())

sigma, mini = 0, 0
for n in range(M, N+1):
    if n == 1:
        continue
    elif is_prime(n):
        sigma += n
        if mini == 0:
            mini = n

if sigma == 0:
    print(-1)
else:
    print(sigma)
    print(mini)

