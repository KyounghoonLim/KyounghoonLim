def match(begin, target, word, num=0):
    global ans

    if begin == target:
        if ans > num:
            ans = num
        return

    for i in range(n):
        if not visited[i]:
            flag = False
            for j in range(len(begin)):
                _begin = begin[:j] + begin[j+1:]
                _target = word[i][:j] + word[i][j+1:]
                if _begin == _target:
                    flag = True
                    break
            if flag:
                visited[i] = True
                match(word[i], target, word, num+1)
                visited[i] = False


def solution(begin, target, words):
    global n
    global visited

    n = len(words)
    visited = [False] * n

    if target not in words:
        return 0

    match(begin, target, words)

    if ans != 987654321:
        return ans
    else:
        return 0


n = None
visited = None
ans = 987654321

print(solution('hit', 'cgg', ["cgg", "dot", "dog", "lot", "log"]))