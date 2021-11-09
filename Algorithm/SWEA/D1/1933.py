user_input = int(input())
temp = list(range(1, user_input+1))
ans = []
for i in temp:
    if user_input % i == 0:
        ans.append(i)

for i in ans:
    if i == user_input:
        print(i)
    else:
        print(i, end=' ')