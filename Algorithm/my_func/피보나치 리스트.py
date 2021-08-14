def fibo_recursive(n):
        if n < 2:
            return 1
        return fibo_recursive(n-2) + fibo_recursive(n-1)

def fibo(num):
    fibo_list = []
    for i in range(num):
        temp = fibo_recursive(i)
        fibo_list.append(temp)
    return fibo_list

print(fibo(10))
