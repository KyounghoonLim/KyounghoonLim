def solution(record):
    answer = []
    user = {}
    for i in range(len(record)):
        record[i] = record[i].split()
        if record[i][0] == 'E':
            user[record[i][1]] = record[i][2]

    for case in record:
        if case[0][0] == 'L':
            answer.append([case[1], '님이 나갔습니다.'])
        else:
            if case[0][0] == 'E':
                answer.append([case[1], '님이 들어왔습니다.'])
            user[case[1]] = case[2]

    for i in range(len(answer)):
        answer[i] = user[answer[i][0]] + answer[i][1]

    return answer