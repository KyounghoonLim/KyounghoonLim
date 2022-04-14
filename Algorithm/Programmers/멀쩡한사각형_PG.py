import math


def solution(w,h):
    answer = w * h

    d = math.sqrt(w ** 2 + h ** 2)
    theta = math.acos(h / d)

    x = 1
    while True:
        y = math.tan(theta) * x
        if math.isclose(y, round(y)):
            break
        x += 1

    

    for n in range(h // x):
        if x == 1:
            answer -= 1
        else:
            answer -= 2 * (x-2) + 2

    return answer

print(solution(2, 2))