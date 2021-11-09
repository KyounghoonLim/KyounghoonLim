def my_min(arr)
    mini = arr[0]
    for t in range(len(arr)):
        if arr[t] > arr[mini]:
            mini = t

    return mini


def move(arr):
    temp = []
    for t in range(3):
        if arr[t]:
            temp.append(arr[t][0])
    m = my_min(temp)



test_case = int(input().strip())
stick = [[],[],[]]
for n in range(test_case):
    stick[0].append(n)