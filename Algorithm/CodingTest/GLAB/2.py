import copy


def put_bricks(arr, n, k, t=0, nums=0):
    global answer
    if t == k - 1:
        if answer > nums:
            answer = nums
            return
    for i in range(1, len(arr[0]) - 1):
        if not arr[0][i] and not arr[0][i-1] and not arr[0][i+1]:
            temp = copy.deepcopy(arr)
            brick = 0
            for j in range(n):
                if temp[j][i]:
                    break
                temp[j][i] = 1
                brick += 1
            put_bricks(temp, n, k, t+1, nums + brick)


def solution(bricks, n, k):
    global answer
    test_case = [[0] * len(bricks) for _ in range(n)]

    for i in range(len(bricks)):
        for j in range(n-1, n-1-bricks[i], -1):
            test_case[j][i] = 1

    put_bricks(copy.deepcopy(test_case), n, k)

    return answer

answer = 987654321