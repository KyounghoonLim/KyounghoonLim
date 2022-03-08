import math

def solution(lines):
    answer = 1
    task = []
    for log in lines:
        log = log.split()
        time = log[1].split(':')
        response_time = 0
        for t in range(len(time)):
            response_time += float(time[t]) * 60 ** (2-t)
        request_time = response_time - float(log[2][:-1]) + float(0.001)
        if task and request_time > task[-1] + float(0.999) and not math.isclose(request_time, task[-1] + float(0.999)):
            if answer < len(task):
                answer = len(task)
            task.pop()
        task = [response_time] + task
    if answer < len(task):
        answer = len(task)

    return answer

print(solution(["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"]))