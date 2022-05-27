def solution(string):
    answer = 0

    for i in range(len(string)):
        for j in range(i+1, len(string)+1):
            if j - i <= answer:
                continue
            temp = string[i:j]
            if temp == temp[::-1]:
                if len(temp) > answer:
                    answer = len(temp)

    return answer

print(solution('abacde'))