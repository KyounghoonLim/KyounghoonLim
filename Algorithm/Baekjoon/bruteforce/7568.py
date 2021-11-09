def who_is_bigger(n):
    order = 1
    for t in range(N):
        if t != n:
            w, h = 0, 0
            if test_case[t][0] > test_case[n][0]:
                w = 1
            if test_case[t][1] > test_case[n][1]:
                h = 1
            if w and h:
                order += 1
    big_man[n] = str(order)


N = int(input().strip())

test_case = [list(map(int, input().strip().split())) for _ in range(N)]
big_man = [0] * N
for i in range(N):
    who_is_bigger(i)

print(' '.join(big_man))