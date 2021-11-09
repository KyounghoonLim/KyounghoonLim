def is_prime(num):
    for t in range(2, num//2 + 1):
        if num % t == 0:
            return

    return True


N = int(input().strip())

test_case = map(int, input().strip().split())
ans = 0
for n in test_case:
    if n == 1:
        continue
    elif is_prime(n):
        ans += 1

print(ans)