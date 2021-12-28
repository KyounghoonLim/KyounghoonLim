for tc in range(1, int(input().strip())+1):
    N, A, B = map(int, input().strip().split())
    if N >= A + B:
        print('#{} {} 0' .format(tc, min((A, B))))
    else:
        print('#{} {} {}' .format(tc, min((A, B)), abs(N-A-B)))