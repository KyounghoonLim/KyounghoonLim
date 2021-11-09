def is_prime(n):
    if n == 1:
        return
    for t in range(2, (n//2)+1):
        if n % t == 0:
            return
    return True


def make_num(n, k):
    temp = 0
    t = 0
    while n > k:
        temp += (n % k) * 10 ** t
        n //= k
        t += 1
    temp += n * 10 ** t
    print(temp)
    temp = list(map(int, str(temp)))

    return temp


def solution(n, k):
    num = make_num(n, k)
    temp = []
    sigma = 0
    answer = 0
    for t in range(len(num)):
        if num[t] > 0:
            temp.append(num[t])
            if t == len(num)-1:
                for t2 in range(len(temp) - 1, -1, -1):
                    sigma += temp[t2] * 10 ** (len(temp) - t2 - 1)
                if is_prime(sigma):
                    answer += 1
        elif temp and num[t] == 0:
            for t2 in range(len(temp)-1, -1, -1):
                sigma += temp[t2] * 10 ** (len(temp) - t2 -1)
            if is_prime(sigma):
                answer += 1
            temp.clear()
            sigma = 0

    return answer

print(solution(437674, 3))