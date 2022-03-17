def solution(money, costs):
    answer = 0
    temp = [1, 5, 10, 50, 100, 500]
    while money > 0:
        same_value = []

        for i in range(len(temp)-1, -1, -1):
            if money < temp[i]:
                temp.pop()
                continue
            tar = len(temp) -1 -i
            if len(temp) % 2 and i % 2:
                same_value.append(costs[tar] * temp[-1] // temp[tar])
            same_value.append(costs[tar] * temp[i])
        answer += money // temp[-1] * min(same_value)
        money %= temp[-1]

    return answer

print(solution(4578, [1, 4, 99, 35, 50, 1000]))