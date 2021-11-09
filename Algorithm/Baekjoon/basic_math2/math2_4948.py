def is_prime(num):
    for t in prime:
        if num == t:
            return True
    for t in range(2, int(num ** 0.5) + 1):
        if num % t == 0:
            return

    prime.add(num)

    return True


prime = set()

while True:
    test_case = int(input().strip())
    if test_case == 0:
        break
    ans = 0

    for n in range(test_case, test_case * 2 + 1):
        if n == 1:
            continue
        elif is_prime(n):
            ans += 1

    print(ans)