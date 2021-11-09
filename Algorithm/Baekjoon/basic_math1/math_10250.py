T = int(input().strip())

for tc in range(T):
    H, W, N = map(int, input().strip().split())
    if N % H:
        filled = str(N % H)
        room = str(N // H + 1)
    else:
        filled = str(H)
        room = str(N // H)

    if len(room) == 1:
        room = '0' + room

    print('{}{}' .format(filled, room))
