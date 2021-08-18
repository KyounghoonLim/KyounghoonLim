T = int(input())
user_input = []
for test_case in range(T):
    user_input.append(int(input()))

ans = []

for case in user_input:
    temp = []
    for i in range(case):
        if i == 0:
            temp.append([1])
        else:
            temp2 = []
            for j in range(i+1):
                if j == 0 or j == i:
                    temp2.append(1)
                else:
                    temp2.append(sum(temp[i-1][j-1:j+1]))
            temp.append(temp2)
    ans.append(temp)

for i in range(len(ans)):
    print(f'#{i+1}')
    for j in range(len(ans[i])):
        for k in range(j+1):
            if k == j:
                print(f'{ans[i][j][k]}')
            else:
                print(f'{ans[i][j][k]}', end=' ')
