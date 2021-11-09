def win(a, b):
    if a[4] > b[4]:
        return 'A'
    elif a[4] == b[4]:
        if a[3] > b[3]:
            return 'A'
        elif a[3] == b[3]:
            if a[2] > b[2]:
                return 'A'
            elif a[2] == b[2]:
                if a[1] > b[1]:
                    return 'A'
                elif a[1] == b[1]:
                    return 'D'

    return 'B'


T = int(input().strip())

for tc in range(T):
    A = list(map(int, input().strip().split()))
    B = list(map(int, input().strip().split()))

    cnt_A = [0] * 5
    cnt_B = [0] * 5
    for t in range(1, len(A)):
        cnt_A[A[t]] += 1
    for t in range(1, len(B)):
        cnt_B[B[t]] += 1

    print(win(cnt_A, cnt_B))
