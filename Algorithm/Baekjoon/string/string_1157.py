def my_sort(arr):
    for t in range(len(arr)-1):
        maxi = t
        for t2 in range(t+1, len(arr)):
            if arr[t2][0] > arr[maxi][0]:
                maxi = t2
        arr[maxi], arr[t] = arr[t], arr[maxi]
    if arr[0][0] == arr[1][0]:
        return '?'
    else:
        return arr[0][1]


test_case = input().strip()
cnt = [[0,chr(i+65)] for i in range(26)]
for text in test_case:
    if ord(text) > 96:
        cnt[ord(text)-97][0] += 1
    else:
        cnt[ord(text)-65][0] += 1
print(my_sort(cnt))