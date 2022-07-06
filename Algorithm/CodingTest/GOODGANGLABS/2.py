def next_round(tar):
    '''
    타겟이 짝수인 경우 나누기 2만큼의 라운드로,
    홀수인 경우 나누기 2 + 1만큼의 라운드로 진출
    '''

    return tar // 2 + tar % 2


def solution(n, a, b):
    answer = 0

    '''
    a, b가 서로 만나는 경우를 체크할 때
    abs(a-b) == 1 인 경우로 한다면,
    a = 2, b = 3 인 경우 버그 발생.
    
    따라서, 만나서 경기를 진행한 이후
    서로의 다음 라운드가 같아지는 경우에
    해당 라운드에서 만났다고 판단할 수 있다. 
    '''
    while a != b:
        answer += 1
        a = next_round(a)
        b = next_round(b)

    return answer


print(solution(8, 4, 7))