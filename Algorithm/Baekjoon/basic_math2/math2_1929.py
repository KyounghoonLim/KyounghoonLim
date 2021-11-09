def is_prime(num):
    for t in range(2, int(num ** 0.5) + 1):
        if num % t == 0:
            return

    return True


M, N = map(int, input().strip().split())
for n in range(M, N+1):
    if n == 1:
        continue
    elif is_prime(n):
        print(n)

