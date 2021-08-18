T = int(input())
user_input = []
for test_case in range(1, T + 1):
    user_input.append(list(map(int,input().split())))

for i in user_input:
    print(max(i))