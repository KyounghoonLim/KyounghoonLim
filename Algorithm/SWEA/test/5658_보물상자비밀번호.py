def hex_to_dec(word):
    result = 0
    hex_table = ['A', 'B', 'C', 'D', 'E', 'F']
    for t in range(len(word)-1, -1, -1):
        if word[t] in hex_table:
            tmp = 10 + hex_table.index(word[t])
        else:
            tmp = int(word[t])
        result += tmp * (16 ** (len(word) - 1 - t))

    return result


def my_sort(arr):
    for t in range(len(arr)):
        arr[t] = hex_to_dec(arr[t])
    for i in range(len(arr)-1):
        maxi = i
        for j in range(i+1, len(arr)):
            if arr[maxi] < arr[j]:
                maxi = j
        arr[maxi], arr[i] = arr[i], arr[maxi]

    return arr


T = int(input().strip())

for tc in range(1, T+1):
    N, K = map(int, input().strip().split())
    test_case = input().strip()

    words = set()
    temp = test_case
    for n in range(N):
        temp = temp[-1] + temp[:-1]
        for t in range(4):
            words.add(temp[t*(N//4):(t+1)*(N//4)])

    ans = my_sort(list(words))
    print('#{} {}' .format(tc, ans[K-1]))