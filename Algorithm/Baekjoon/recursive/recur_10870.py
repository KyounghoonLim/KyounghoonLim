# def fibo(n):
#     if len(arr) > n:
#         return arr[n]
#     a = fibo(n-2)
#     b = fibo(n-1)
#     arr.append(a+b)
#     return arr[n]
#
# arr = [1, 1]
# test_case = int(input().strip())
# fibo(test_case)
# print(arr[test_case-1])
#####################################
def fibo(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    return fibo(n-2) + fibo(n-1)

test_case = int(input().strip())
print(fibo(test_case))