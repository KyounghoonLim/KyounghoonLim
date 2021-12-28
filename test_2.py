def remove_repeat(arr):
    for ans_set in ans[target]:
        flag = len(arr)
        if len(ans_set) == len(arr):
            for t in range(len(arr)):
                if ans_set[t] == arr[t]:
                    flag -= 1
        if not flag:
            return
    return True


def combination(comb_target, result=[], idx_nums=0):
    if comb_target == 0:    # 원하는 갯수의 집단을 구했을 경우
        tmp = sorted(result)
        if remove_repeat(tmp):
            ans[target].append(tmp)  # 결과에 포함
        return
    for t in range(N):
        if not visited[t]:
            visited[t] = 1  # 해당 컬럼은 사용했음
            result.append(test_case[t]) # 해당 컬럼 추가
            combination(comb_target-1, result, idx_nums+t)  # 재귀함수 호출
            result.pop()    # 해당 컬럼 삭제
            visited[t] = 0  # 다른 경우의 수 판단해야하니 사용 해제


# N = 10  # 데이터 갯수 지정

test_case = input().strip().split() # 컬럼 이름 리스트에 채우기
N = len(test_case)
visited = [0] * N   # 해당 컬럼을 사용했는지 체크

ans = [[] for _ in range(N)]    # 결과

for target in range(1, N): # 1개 부터 N-1개 까지의 조합을 돌려볼 것
    combination(target)

reverse_ans = []    # 가져간 집단의 반대 집단 구하는 코드
for i in range(len(ans)):
    temp = []
    for j in range(N):
        if test_case[j] not in ans[i]:
            temp.append(test_case[j])
    reverse_ans.append(temp)

print(ans)
print(reverse_ans)
##### ans의 1번 집단 사용할 경우 reverse_ans의 1번 집단 사용하면 됨.