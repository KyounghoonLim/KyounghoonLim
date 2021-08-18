T = int(input())
user_input = []
for test_case in range(1, T + 1):
    user_input.append(list(map(int, input().split())))
i = 0
for j in user_input:
    i += 1
    Q = j[0] // j[1]
    R = j[0] % j[1]
    print(f'#{i} {Q} {R}')
