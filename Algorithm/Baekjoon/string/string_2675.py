T = int(input().strip())

for tc in range(1, T+1):
    temp = input().strip().split()
    N = int(temp[0])
    test_case = temp[1]

    for text in test_case:
        for n in range(N):
            print(text, end='')
    print()