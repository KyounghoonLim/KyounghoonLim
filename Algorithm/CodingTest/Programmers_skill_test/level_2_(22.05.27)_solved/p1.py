def solution(prices):
    answer = [0] * len(prices)

    for i in range(len(prices)):
        t = 0
        for j in range(i+1, len(prices)):
            t += 1
            if prices[i] > prices[j]:
                break
        answer[i] = t

    return answer

print(solution([1,2,3,2,3]))