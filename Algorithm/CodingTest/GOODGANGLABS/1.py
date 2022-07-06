def solution(nums):
    n = len(nums) // 2

    ### 몬스터 종류의 수 ###
    monster = set(nums)

    ### 몬스터 종류가 뽑을 수 보다 많다면 ###
    if len(monster) > n:
        return n
    ### 뽑을 수보다 적다면 ###
    else:
        return len(monster)