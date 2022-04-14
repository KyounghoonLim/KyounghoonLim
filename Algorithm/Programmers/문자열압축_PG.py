def solution(s):
    ans = len(s)

    for i in range(1, len(s)//2 + 1):
        keyword = s[:i]
        count = 0
        result = ''
        for j in range(0, len(s)+1, i):
            if j < len(s) and keyword == s[j:j+i]:
                count += 1
            else:
                if count != 1:
                    result += str(count) + keyword
                else:
                    result += keyword
                if j < len(s):
                    keyword = s[j:j+i]
                    count = 1

        if len(keyword) < i:
            result += keyword

        if len(result) < ans:
            ans = len(result)

    return ans