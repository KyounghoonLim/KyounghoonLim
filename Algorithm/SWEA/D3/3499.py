T = int(input().strip())

for tc in range(1, T + 1):
    N = int(input().strip())
    test_case = input().strip().split()

    left = test_case[:N // 2 + N % 2]
    right = test_case[N // 2 + N % 2:]
    deck = []
    while len(right) > 0:
        if len(left) > len(right):
            deck.append(left.pop())
            deck.append(right.pop())
        else:
            deck.append(right.pop())
            deck.append(left.pop())
    if left:
        deck.append(left.pop())
    ans = ' '.join(deck[::-1])

    print('#{} {}' .format(tc, ans))