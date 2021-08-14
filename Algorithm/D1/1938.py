user_input = list(map(int, (input().split())))
a, b = user_input[0], user_input[1]
ans = [a+b, a-b, a*b, a/b]
for i in ans:
    print(int(i))