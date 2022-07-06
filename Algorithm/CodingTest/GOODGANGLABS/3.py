def find_index(my_num, target):
    ### 상대방 배열 뒤에서부터 순회(list.pop() 최적화) ###
    for i in range(len(target)-1, -1, -1):
        ### 현재 내 숫자보다 크거나 같은 값 발견시 ###
        if my_num <= target[i]:
            ### 만약 내 숫자가 상대방의 가장 작은 숫자보다 작을 경우 루프 종료 ###
            if i == len(target) - 1:
                break
            return i + 1
    ### 내 숫자보다 작은 값 존재하지 않을 경우 첫 번째 인덱스 반환 ###
    return 0


def solution(A, B):
    answer = 0

    ### 상대방 배열 내림차순, 내 배열 오름차순 정렬(list.pop() 최적화) ###
    target = sorted(A, reverse=True)
    my_nums = sorted(B)

    for my_num in my_nums:
        ### 내가 이길 수 있는 상대방의 값 인덱스 조회 ###
        target_idx = find_index(my_num, target)
        ### 상대방의 숫자가 나보다 작으면 ###
        if my_num > target[target_idx]:
            answer += 1
        target.pop(target_idx)

    return answer

# print(solution([5,1,3,7], [2,2,6,8]))
# print(solution([2,2,2,2], [1,1,1,1]))
# print(solution([2,1,4,3], [2,3,3,1]))