T = int(input())
user_input = []
ans = []

for test_case in range(1, T + 1):
    temp_input = [int(input())]
    temp_input.extend(list(map(int, input().split())))
    user_input.append(temp_input)

for business in user_input:
    total_temp = []
    for i in range(1, business[0]):
        temp = business[1:i+1]
        for j in range(len(temp)-1, -1, -1):
            if temp[j] > business[i]:
                temp.pop(j)
        margin = business[i+1] * len(temp) - sum(temp)
        if margin < 0:
            total_temp.append(0)
        total_temp.append(margin)
    max_margin = max(total_temp)
    ans.append(max_margin)

i = 1

for k in ans:
    print(f'#{i} {k}')
    i += 1

