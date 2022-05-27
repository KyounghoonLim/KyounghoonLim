def solution(replies, n, k):
    answer = [1] * len(replies)
    for idx in range(len(replies)):
        reply = replies[idx]
        max_length = len(reply) // k
        flag = False
        for l in range(n, max_length+1):
            if flag:
                break
            for i in range(len(reply) - l * (k - 1)):
                if flag:
                    break
                context = reply[i:i+l]
                num = 1
                for j in range(1, k):
                    if reply[i+l*j:i+l*(j+1)] != context:
                        break
                    num += 1
                if num == k:
                    flag = True
        if flag:
            answer[idx] = 0

    return answer

inp = ["FFCCAAFCCAAA", "AAAABBBBCCCC", "ABCABCABCABC"]
print(solution(inp, 4, 2))