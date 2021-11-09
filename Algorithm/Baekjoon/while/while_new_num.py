test_case = input().strip() #문자열로 받음(인덱싱위해서)
Q = [0, 0]  #Q초기화
cnt = 0 #사이클 횟수
for t in range(1, len(test_case) + 1):  #인풋이 한자릿수일 경우를 대비해서 뒤에서 접근
    Q[-t] = int(test_case[-t])
while True:
    temp = str(Q[0] + Q[1]) #우선 사이클도 인덱싱을 위해 문자열로 담음
    Q[0] = Q[1]
    Q[1] = int(temp[-1])
    cnt += 1
    if int(test_case) == Q[0] * 10 + Q[1]:
        print(cnt)
        break
