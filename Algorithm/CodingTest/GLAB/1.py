def solution(n, text, second):

    blank_time = len(text) + n
    remain_time = second % blank_time
    if not remain_time or not second:
        answer = ' ' * n
    else:
        _text = ' ' * n + text + ' ' * n
        answer = _text[remain_time:remain_time+n]

    return answer.replace(' ', '_')