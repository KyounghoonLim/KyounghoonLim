def writing(idx):
    for t in range(idx, len(temp)):
        temp[t] += 1    #각 지점에 1 더한다
        if temp[t] > 1: #만일 1보다 커질 경우, 2진수이므로 자릿수 올림 발생
            temp[t] = 0
            if t < len(temp)-1: #인덱스에러 방지
                temp[t+1] += 1


def find_target(idx, start=0):
    for t in range(start, len(test_case)):
        if test_case[t] == idx:
            return t


def min_memory():
    cnt, tar, flag = 0, 0, 0    #초기화
    while True:
        tar = find_target(1 - flag, tar)    #시작점 찾기. 함수호출 line: 10
        writing(tar)    #해당 지점부터 메모리 덮어쓰기. 함수호출 line: 1
        cnt += 1    #시행횟수 더함
        if temp == test_case:
            return cnt
        else:
            flag = 1 - flag #다음 타겟은 1, 0 둘 중 스위치 된 값


T = int(input().strip())

for tc in range(1, T+1):
    test_case = list(map(int, input().strip()))
    temp = [0] * len(test_case) #초기화된 메모리

    print('#{} {}' .format(tc, min_memory()))   #함수호출 line: 16