def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)


test_case = int(input().strip())

print(factorial(test_case))